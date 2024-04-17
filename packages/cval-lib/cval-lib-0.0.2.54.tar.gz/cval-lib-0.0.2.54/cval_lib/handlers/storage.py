"""
Introducing CVAL Rest API, a powerful tool for AI developers in the computer vision field.
Our service combines the concepts of human-in-the-loop and active learning to improve the quality of
your models and minimize annotation costs for classification, detection, and segmentation cases.

With CVAL, you can iteratively improve your models by following our active learning loop.
First, manually or semi-automatically annotate a random set of images.
Next, train your model and use uncertainty and diversity methods to score the remaining images for annotation.
Then, manually or semi-automatically annotate the images marked as more confident to increase the accuracy of the model.
Repeat this process until you achieve an acceptable quality of the model.

Our service makes it easy to implement this workflow and improve your models quickly and efficiently.
Try our demo notebook to see how CVAL can revolutionize your computer vision projects.

To obtain a client_api_key, please send a request to k.suhorukov@digital-quarters.com
"""

from requests import Session

from cval_lib.configs.main_config import MainConfig
from cval_lib.handlers._abstract_handler import AbstractHandler
from cval_lib.models.storage import CloudStorageModelWithID, CloudStorageModel


class Storage(AbstractHandler):
    def __init__(
            self,
            session: Session,
            _id: str = None
    ):
        self.route = f'{MainConfig.main_url}/api/cloud'
        super().__init__(session, )
        self._id = _id

    def get_all(self):
        self._get(f'{self.route}/all')
        return list(map(lambda x: CloudStorageModelWithID(**x), self.send().json()))

    def get(self, _id: str = None):
        self._get(f'{self.route}/{_id or self._id}')
        return CloudStorageModelWithID(**self.send().json())

    def create(
            self,
            access_key: str,
            secret_key: str,
            endpoint: str,
            bucket: str,
            synchronize: bool = True,
    ):
        self._post(
            f'{self.route}',
            json=CloudStorageModel(
                access_key=access_key,
                secret_key=secret_key,
                endpoint=endpoint,
                bucket=bucket,
                synchronize=synchronize,
            ).dict()
        )
        self._id = self.send().get('id')
        return self._id

    def delete(self, _id: str):
        self._delete(f'{self.route}/{_id or self._id}')
        return self.send().json()

    def change_sync(self, _id: str, synchronize: bool):
        self._put(f'{self.route}/{_id or self._id}', params={'synchronize': synchronize})
        return self.send().json()
