from datetime import datetime
from uuid import UUID

from fiddler3.schemas.base import BaseModel
from fiddler3.schemas.organization import OrganizationCompactResp


class ProjectCompactResp(BaseModel):
    id: UUID
    name: str


class ProjectResp(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime

    organization: OrganizationCompactResp
