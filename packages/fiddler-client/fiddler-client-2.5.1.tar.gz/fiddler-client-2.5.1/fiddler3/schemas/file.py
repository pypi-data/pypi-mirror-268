from datetime import datetime
from uuid import UUID

from pydantic import Field

from fiddler3.schemas.base import BaseModel
from fiddler3.schemas.user import UserCompactResp


class FileResp(BaseModel):
    id: UUID
    name: str = Field(alias='filename')
    status: str
    type: str
    created_at: datetime
    updated_at: datetime
    created_by: UserCompactResp
    updated_by: UserCompactResp


class FileCompactResp(BaseModel):
    id: UUID
    name: str
