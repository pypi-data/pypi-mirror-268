from typing import Optional
from uuid import UUID

from fiddler3.constants.dataset import EnvType
from fiddler3.schemas.base import BaseModel
from fiddler3.schemas.model import ModelCompactResp
from fiddler3.schemas.organization import OrganizationCompactResp
from fiddler3.schemas.project import ProjectCompactResp


class DatasetCompactResp(BaseModel):
    """Dataset Compact."""

    id: UUID
    name: str
    type: EnvType


class DatasetResp(BaseModel):
    """Dataset response pydantic model."""

    id: UUID
    name: str
    row_count: Optional[int]
    model: ModelCompactResp
    project: ProjectCompactResp
    organization: OrganizationCompactResp
