from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID

from fiddler3.decorators import handle_api_error
from fiddler3.entities.base import BaseEntity
from fiddler3.entities.project import ProjectCompactMixin
from fiddler3.schemas.model_deployment import ModelDeploymentResponse
from fiddler3.utils.logger import get_logger

logger = get_logger(__name__)


class ModelDeployment(
    BaseEntity, ProjectCompactMixin
):  # pylint: disable=too-many-instance-attributes
    def __init__(  # pylint: disable=too-many-arguments
        self,
        model_id: UUID,
    ) -> None:
        """Construct a model deployment instance."""
        self.id: UUID | None = None  # pylint: disable=invalid-name
        self.model_id = model_id
        self.artifact_type: str | None = None
        self.deployment_type: str | None = None
        self.active: bool | None = None
        self.image_uri: str | None = None
        self.replicas: int | None = None
        self.cpu: int | None = None
        self.memory: int | None = None
        self.created_at: datetime | None = None
        self.updated_at: datetime | None = None

        # Deserialized response object
        self._resp: ModelDeploymentResponse | None = None

    @staticmethod
    def _get_url(model_id: UUID | str) -> str:
        """Get model deployment url."""
        return f'v3/models/{model_id}/deployment'

    @classmethod
    def _from_dict(cls, data: dict) -> ModelDeployment:
        """Build entity object from the given dictionary."""

        # Deserialize the response
        resp_obj = ModelDeploymentResponse(**data)
        # Initialize
        instance = cls(
            model_id=resp_obj.model.id,
        )

        # Add remaining fields
        fields = [
            'id',
            'artifact_type',
            'deployment_type',
            'active',
            'image_uri',
            'replicas',
            'cpu',
            'memory',
            'created_at',
            'updated_at',
        ]
        for field in fields:
            setattr(instance, field, getattr(resp_obj, field, None))

        instance._resp = resp_obj
        return instance

    def _refresh(self, data: dict) -> None:
        """Refresh the fields of this instance from the given response dictionary"""
        # Deserialize the response
        resp_obj = ModelDeploymentResponse(**data)

        fields = [
            'id',
            'artifact_type',
            'deployment_type',
            'active',
            'image_uri',
            'replicas',
            'cpu',
            'memory',
            'created_at',
            'updated_at',
        ]
        for field in fields:
            setattr(self, field, getattr(resp_obj, field, None))

        self._resp = resp_obj

    @handle_api_error
    def update(self) -> None:
        """Update an existing model deployment."""
        body: dict[str, Any] = {
            'artifact_type': self.artifact_type,
            'deployment_type': self.deployment_type,
            'active': self.active,
            'image_uri': self.image_uri,
            'replicas': self.replicas,
            'cpu': self.cpu,
            'memory': self.memory,
        }

        response = self._client().patch(
            url=self._get_url(model_id=self.model_id), data=body
        )
        self._refresh_from_response(response=response)

    @classmethod
    def of(cls, model_id: UUID) -> ModelDeployment:
        """
        Get model deployment instance of the given model

        :param model_id: Model identifier
        :return: ModelDeployment instance
        """
        response = cls._client().get(url=cls._get_url(model_id=model_id))
        return cls._from_dict(data=response.json()['data'])
