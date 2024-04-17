from typing import Any
from uuid import UUID

from simplejson import JSONEncoder


class RequestClientJSONEncoder(JSONEncoder):
    def default(self, o: Any) -> Any:
        """Override JSONEncoder.default to support uuid serialization"""
        if isinstance(o, UUID):
            return str(o)
        return super().default(o)
