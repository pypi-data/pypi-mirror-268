from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from fiddler3.schemas.base import BaseModel
from fiddler3.schemas.dataset import DatasetCompactResp
from fiddler3.schemas.model import ModelCompactResp
from fiddler3.schemas.organization import OrganizationCompactResp
from fiddler3.schemas.project import ProjectCompactResp


class BaselineCompactResp(BaseModel):
    id: UUID
    name: str


class BaselineResp(BaseModel):
    """Baseline response pydantic model."""

    id: UUID
    name: str
    type: str
    start_time: Optional[int]
    end_time: Optional[int]
    offset: Optional[int]
    window_size: Optional[int]
    row_count: Optional[int]

    model: ModelCompactResp
    project: ProjectCompactResp
    organization: OrganizationCompactResp
    dataset: DatasetCompactResp = Field(alias='environment')

    created_at: datetime
    updated_at: datetime
