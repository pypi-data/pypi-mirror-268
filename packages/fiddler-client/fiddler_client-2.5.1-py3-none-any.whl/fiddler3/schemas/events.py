from typing import Any, Dict, List
from uuid import UUID

from fiddler3.constants.events import PublishEventsSourceType
from fiddler3.schemas.base import BaseModel


class FileSource(BaseModel):
    file_id: UUID
    type: PublishEventsSourceType = PublishEventsSourceType.FILE


class EventsSource(BaseModel):
    events: List[Dict[Any, Any]]
    type: PublishEventsSourceType = PublishEventsSourceType.EVENTS
