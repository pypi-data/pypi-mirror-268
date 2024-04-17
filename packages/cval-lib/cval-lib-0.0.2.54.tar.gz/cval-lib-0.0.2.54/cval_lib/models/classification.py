from __future__ import annotations

from typing import Optional, List

from pydantic import validator, BaseModel, Field

from cval_lib.models._base import ExecModel, fields
from cval_lib.models.detection import BBoxScores as _BBoxScores, FramePrediction as _DetFramePrediction, \
    DetectionSamplingOnPremise
from cval_lib.models.weights import WeightsConfigModel


@fields(
    'weights_of_model',
    'model',
    'use_pretrain_model = True',
    'use_backbone_freezing = False',
)
class ClassificationTest(ExecModel):
    """
    :param weights_of_model to be used in active learning or evaluation
    :param model: type of the model. Currently, supports: b0, resnet50, mobilenet
    :param use_pretrain_model : Whether to use a pre-trained model or not
    :param use_backbone_freezing: Whether to use backbone freezing in the training process
    """
    weights_of_model: Optional[WeightsConfigModel]
    model: str
    n_epochs: int = 1000
    use_pretrain_model: bool = True
    use_backbone_freezing: bool = False
    early_stopping_num_epochs: int = 50
    validation_step: int = 2
    use_validation: bool = True

    def send(self, user_api_key: str, dataset_id: str, sync: bool = True):
        return self._send(user_api_key, f'/dataset/{dataset_id}/test/classification', sync)

    @validator('model')
    def validate_model(cls, value):
        allowed = ['b0', 'resnet50', 'mobilenet']
        if value not in allowed:
            raise ValueError(f"Invalid name: {value}. Allowed models are: {', '.join(allowed)}")
        return value


@fields(
    'num_samples: int',
    'weights_of_model: WeightsConfigModel = None',
    'batch_unlabeled: int',
    'model: str',
    'selection_strategy: str',
    'use_pretrain_model: bool = True',
    'use_backbone_freezing: bool = False',
)
class ClassificationSampling(ExecModel):
    """
    :param weights_of_model to be used in active learning or evaluation
    :param num_samples: absolute number of samples to select
    :param n_epochs: number of model training epochs
    :use_validation: whether to use validation during training or not
    :param batch_unlabeled: the limit of unlabeled samples that can be processed during selection
    :param model: type of the model. Currently, supports: b0, resnet50, mobilenet
    :param use_pretrain_model : Whether to use a pre-trained model or not
    :param use_backbone_freezing: Whether to use backbone freezing in the training process
    """
    num_samples: int
    n_epochs: int = 1000
    weights_of_model: Optional[WeightsConfigModel]
    batch_unlabeled: int
    model: str
    selection_strategy: str
    use_pretrain_model: bool = True
    use_backbone_freezing: bool = False
    use_validation: bool = True
    early_stopping_num_epochs: int = 50
    validation_step: int = 2

    def send(self, user_api_key: str, dataset_id: str, sync: bool = True):
        return self._send(user_api_key, f'/dataset/{dataset_id}/sampling/classification', sync)

    @validator('selection_strategy')
    def validate_selection_strategy(cls, value):
        allowed = ['margin', 'least', 'ratio', 'entropy', 'vae', 'mixture']
        if value not in allowed:
            raise ValueError(f"Invalid name: {value}. Allowed selection strategies are: {', '.join(allowed)}")
        return value


class FrameScore(BaseModel):
    category_id: Optional[int]
    score: Optional[float]
    embedding_id: Optional[str]
    probabilities: Optional[List[float]]


@fields(
    'frame_id: str',
    'predictions: Optional[List[BBoxScores]]'
)
class CLSFramePrediction(BaseModel):
    """
    :param frame_id: id of the frame
    :param prediction: frame score
    """
    frame_id: str = Field(max_length=128)
    prediction: FrameScore


class ClassificationSamplingOnPremise(ExecModel):
    num_of_samples: int
    num_of_clusters: int = -1
    selection_strategy: str
    dataset_id: Optional[str]
    probs_weights: Optional[List[float]]
    sort_strategy: Optional[str]
    frames: List[CLSFramePrediction]

    def _prepare_for_request(self):
        dct = self.dict()

        frames = [
            _DetFramePrediction(
                frame_id=f.frame_id,
                predictions=[
                    [
                        _BBoxScores(
                            category_id=f.prediction.category_id,
                            score=f.prediction.score,
                            embedding_id=f.prediction.embedding_id,
                            probabilities=f.prediction.probabilities,
                        )
                    ]
                ]
            )
            for f in self.frames
        ]
        dct['frames'] = frames
        return dct

    def send(self, user_api_key: str, sync: bool = True):
        return self._send(user_api_key, '/api/on-premise/sampling/detection', sync)
