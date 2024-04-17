import enum
from typing import Optional

from fiddler3.schemas.base import BaseModel


@enum.unique
class ArtifactType(str, enum.Enum):
    SURROGATE = 'SURROGATE'
    PYTHON_PACKAGE = 'PYTHON_PACKAGE'


@enum.unique
class DeploymentType(str, enum.Enum):
    BASE_CONTAINER = 'BASE_CONTAINER'
    MANUAL = 'MANUAL'


class DeploymentParams(BaseModel):
    artifact_type: str = ArtifactType.PYTHON_PACKAGE
    deployment_type: DeploymentType
    image_uri: Optional[str]
    replicas: Optional[int]
    cpu: Optional[int]
    memory: Optional[int]
