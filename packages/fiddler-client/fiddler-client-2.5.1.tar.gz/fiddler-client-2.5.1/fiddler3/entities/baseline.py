from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Iterator
from uuid import UUID

from fiddler3.constants.dataset import EnvType
from fiddler3.decorators import handle_api_error
from fiddler3.entities.base import BaseEntity
from fiddler3.entities.dataset import DatasetCompactMixin
from fiddler3.entities.model import ModelCompactMixin
from fiddler3.entities.project import ProjectCompactMixin
from fiddler3.schemas.baseline import BaselineResp
from fiddler3.schemas.filter_query import OperatorType, QueryCondition, QueryRule
from fiddler3.utils.helpers import raise_not_found


class Baseline(
    BaseEntity, ModelCompactMixin, ProjectCompactMixin, DatasetCompactMixin
):  # pylint: disable=too-many-instance-attributes
    def __init__(  # pylint: disable=too-many-arguments
        self,
        name: str,
        model_id: UUID,
        environment: EnvType,
        type_: str,
        dataset_id: UUID | None = None,
        start_time: int | None = None,
        end_time: int | None = None,
        offset: int | None = None,
        window_size: int | None = None,
    ) -> None:
        """Construct a baseline instance."""
        self.name = name
        self.model_id = model_id
        self.type = type_
        self.environment = environment
        self.dataset_id = dataset_id
        self.start_time = start_time
        self.end_time = end_time
        self.offset = offset
        self.window_size = window_size

        self.id: UUID | None = None
        self.row_count: int | None = None
        self.project_id: UUID | None = None
        self.create_at: datetime | None = None
        self.updated_at: datetime | None = None

        # Deserialized response object
        self._resp: BaselineResp | None = None

    @staticmethod
    def _get_url(id_: UUID | str | None = None) -> str:
        """Get model resource/item url."""
        url = '/v3/baselines'
        return url if not id_ else f'{url}/{id_}'

    @classmethod
    def _from_dict(cls, data: dict) -> Baseline:
        """Build entity object from the given dictionary."""

        # Deserialize the response
        resp_obj = BaselineResp(**data)

        # Initialize
        instance = cls(
            name=resp_obj.name,
            model_id=resp_obj.model.id,
            environment=resp_obj.dataset.type,
            dataset_id=resp_obj.dataset.id,
            type_=resp_obj.type,
            start_time=resp_obj.start_time,
            end_time=resp_obj.end_time,
            offset=resp_obj.offset,
            window_size=resp_obj.window_size,
        )

        # Add remaining fields
        fields = [
            'id',
            'created_at',
            'updated_at',
            'row_count',
        ]
        for field in fields:
            setattr(instance, field, getattr(resp_obj, field, None))

        instance.project_id = resp_obj.project.id
        instance._resp = resp_obj

        return instance

    def _refresh(self, data: dict) -> None:
        """Refresh the fields of this instance from the given response dictionary"""
        # Deserialize the response
        resp_obj = BaselineResp(**data)

        # Reset properties
        self.model_id = resp_obj.model.id
        self.environment = resp_obj.dataset.type
        self.dataset_id = resp_obj.dataset.id

        # Add remaining fields
        fields = [
            'id',
            'name',
            'type',
            'start_time',
            'end_time',
            'offset',
            'window_size',
            'created_at',
            'updated_at',
            'row_count',
        ]
        for field in fields:
            setattr(self, field, getattr(resp_obj, field, None))

        self._resp = resp_obj

    @classmethod
    @handle_api_error
    def get(cls, id_: UUID | str) -> Baseline:
        """
        Get the baseline instance using baseline id.

        :param id_: unique uuid format identifier for baseline
        :return: baseline instance
        """
        response = cls._client().get(url=cls._get_url(id_=id_))
        return cls._from_response(response=response)

    @classmethod
    @handle_api_error
    def from_name(cls, name: str, model_name: str, project_name: str) -> Baseline:
        """
        Get the baseline instance using baseline name, model name and project name.

        :param name: Baseline name
        :param model_name: Name of the model associated with the baseline
        :param project_name: Name of the project associated with the baseline
        :return: Baseline instance for the provided params
        """

        _filter = QueryCondition(
            rules=[
                QueryRule(field='name', operator=OperatorType.EQUAL, value=name),
                QueryRule(
                    field='project_name',
                    operator=OperatorType.EQUAL,
                    value=project_name,
                ),
                QueryRule(
                    field='model_name', operator=OperatorType.EQUAL, value=model_name
                ),
            ]
        )

        response = cls._client().get(
            url=cls._get_url(),
            params={'filter': _filter.json()},
        )
        if response.json()['data']['total'] == 0:
            raise_not_found('Baseline not found for the given identifier')

        return cls._from_dict(data=response.json()['data']['items'][0])

    @classmethod
    @handle_api_error
    def list(cls) -> Iterator[Baseline]:
        """Get a list of all baselines in the organization."""
        params: dict[str, Any] = {}

        for baseline in cls._paginate(url=cls._get_url(), params=params):
            yield cls._from_dict(data=baseline)

    @handle_api_error
    def create(self) -> Baseline:
        """Create a new baseline."""
        payload = {
            'name': self.name,
            'model_id': self.model_id,
            'type': self.type,
            'env_type': self.environment,
            'env_id': self.dataset_id,
        }
        if self.start_time:
            payload['start_time'] = self.start_time
        if self.end_time:
            payload['end_time'] = self.end_time
        if self.offset:
            payload['offset'] = self.offset
        if self.window_size:
            payload['window_size'] = self.window_size

        response = self._client().post(
            url=self._get_url(),
            data=payload,
        )
        self._refresh_from_response(response=response)
        return self

    @handle_api_error
    def delete(self) -> None:
        """Delete a baseline."""
        assert self.id is not None

        self._client().delete(url=self._get_url(id_=self.id))


@dataclass
class BaselineCompact:
    id: UUID
    name: str

    def fetch(self) -> Baseline:
        """Fetch baseline instance"""
        return Baseline.get(id_=self.id)


class BaselineCompactMixin:
    @property
    def baseline(self) -> BaselineCompact:
        """Baseline instance"""
        response = getattr(self, '_resp', None)
        if not response or not hasattr(response, 'baseline'):
            raise AttributeError(
                'This property is available only for objects generated from API '
                'response.'
            )

        return BaselineCompact(id=response.baseline.id, name=response.baseline.name)
