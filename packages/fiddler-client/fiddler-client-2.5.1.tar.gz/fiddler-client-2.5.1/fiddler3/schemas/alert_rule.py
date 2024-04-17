from datetime import datetime
from typing import List, Optional, Union
from uuid import UUID

from pydantic import Field

from fiddler3.constants.alert_rule import AlertCondition, BinSize, CompareTo, Priority
from fiddler3.schemas.base import BaseModel
from fiddler3.schemas.baseline import BaselineCompactResp
from fiddler3.schemas.model import ModelCompactResp
from fiddler3.schemas.project import ProjectCompactResp


class AlertRuleResp(BaseModel):
    id: UUID = Field(alias='uuid')
    name: str
    model: ModelCompactResp
    project: ProjectCompactResp
    baseline: Optional[BaselineCompactResp]
    priority: Union[str, Priority]
    compare_to: Union[str, CompareTo]
    metric_id: Union[str, UUID] = Field(alias='metric')
    critical_threshold: float
    condition: Union[str, AlertCondition]
    bin_size: Union[str, BinSize]
    columns: Optional[List[str]]
    baseline_id: Optional[UUID]
    compare_bin_delta: Optional[int]
    warning_threshold: Optional[float]

    created_at: datetime
    updated_at: datetime = Field(alias='last_updated')


class NotificationConfig(BaseModel):
    emails: Optional[List[str]]
    pagerduty_services: Optional[List[str]]
    pagerduty_severity: Optional[str]
    webhooks: Optional[List[UUID]]
