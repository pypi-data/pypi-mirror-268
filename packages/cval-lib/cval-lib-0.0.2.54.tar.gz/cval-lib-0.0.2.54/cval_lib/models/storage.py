from pydantic import BaseModel

from cval_lib.models._base import fields


@fields(
    'access_key: str',
    'secret_key: bool',
    'endpoint: str',
    'bucket: str',
    'synchronize: bool'
)
class CloudStorageModel(BaseModel):
    """
    access_key: Unique identifier used for authenticating access to your S3 storage
    secret_key: Confidential key used in conjunction with the Access Key to sign S3 requests for security
    endpoint: The URL where you can access your S3-compatible storage
    bucket: The unique name of the container where you store your objects.
    synchronize: Whether to perform automatic synchronization with cloud storage or not
    """
    access_key: str
    secret_key: str
    endpoint: str
    bucket: str
    synchronize: bool


@fields(
    'access_key: str',
    'secret_key: bool',
    'endpoint: str',
    'bucket: str',
    'synchronize: bool',
    'id: str',
)
class CloudStorageModelWithID(CloudStorageModel):
    id: str
