from __future__ import annotations

import builtins
import typing
from dataclasses import dataclass
from datetime import datetime
from functools import cached_property
from pathlib import Path
from typing import Any, Iterator
from uuid import UUID

import pandas as pd

from fiddler3.constants.dataset import EnvType
from fiddler3.constants.model import ModelInputType, ModelTask
from fiddler3.decorators import handle_api_error
from fiddler3.entities.base import BaseEntity
from fiddler3.entities.events import EventPublisher
from fiddler3.entities.job import Job
from fiddler3.entities.model_artifact import ModelArtifact
from fiddler3.entities.model_deployment import ModelDeployment
from fiddler3.entities.project import ProjectCompactMixin
from fiddler3.entities.surrogate import Surrogate
from fiddler3.entities.user import CreatedByMixin, UpdatedByMixin
from fiddler3.entities.xai import XaiMixin
from fiddler3.schemas.deployment_params import DeploymentParams
from fiddler3.schemas.filter_query import OperatorType, QueryCondition, QueryRule
from fiddler3.schemas.job import JobCompactResp
from fiddler3.schemas.model import ModelResp
from fiddler3.schemas.model_schema import ModelSchema
from fiddler3.schemas.model_spec import ModelSpec
from fiddler3.schemas.model_task_params import ModelTaskParams
from fiddler3.schemas.xai_params import XaiParams
from fiddler3.utils.helpers import raise_not_found
from fiddler3.utils.model_schema_generator import SchemaGeneratorFactory

if typing.TYPE_CHECKING:
    from fiddler3.entities.dataset import Dataset


class Model(
    BaseEntity,
    CreatedByMixin,
    ProjectCompactMixin,
    UpdatedByMixin,
    XaiMixin,
):  # pylint: disable=too-many-ancestors
    def __init__(  # pylint: disable=too-many-arguments
        self,
        name: str,
        project_id: UUID,
        schema: ModelSchema,
        spec: ModelSpec,
        input_type: str = ModelInputType.TABULAR,
        task: str = ModelTask.NOT_SET,
        task_params: ModelTaskParams | None = None,
        description: str | None = None,
        event_id_col: str | None = None,
        event_ts_col: str | None = None,
        event_ts_format: str | None = None,
        xai_params: XaiParams | None = None,
    ) -> None:
        """Construct a model instance"""
        self.name = name
        self.project_id = project_id
        self.schema = schema
        self.input_type = input_type
        self.task = task
        self.description = description
        self.event_id_col = event_id_col
        self.event_ts_col = event_ts_col
        self.event_ts_format = event_ts_format
        self.spec = spec
        self.task_params = task_params or ModelTaskParams()
        self.xai_params = xai_params or XaiParams()

        self.id: UUID | None = None
        self.artifact_status: str | None = None
        self.artifact_files: list[dict] | None = None
        self.is_binary_ranking_model: bool | None = None
        self.created_at: datetime | None = None
        self.updated_at: datetime | None = None

        # Deserialized response object
        self._resp: ModelResp | None = None

    @staticmethod
    def _get_url(id_: UUID | str | None = None) -> str:
        """Get model resource/item url."""
        url = '/v3/models'
        return url if not id_ else f'{url}/{id_}'

    @classmethod
    def _from_dict(cls, data: dict) -> Model:
        """Build entity object from the given dictionary."""

        # Deserialize the response
        resp_obj = ModelResp(**data)

        # Initialize
        instance = cls(
            name=resp_obj.name,
            schema=resp_obj.schema_,
            spec=resp_obj.spec,
            project_id=resp_obj.project.id,
            input_type=resp_obj.input_type,
            task=resp_obj.task,
            task_params=resp_obj.task_params,
            description=resp_obj.description,
            event_id_col=resp_obj.event_id_col,
            event_ts_col=resp_obj.event_ts_col,
            event_ts_format=resp_obj.event_ts_format,
            xai_params=resp_obj.xai_params,
        )

        # Add remaining fields
        fields = [
            'id',
            'created_at',
            'updated_at',
            'artifact_status',
            'artifact_files',
            'is_binary_ranking_model',
        ]
        for field in fields:
            setattr(instance, field, getattr(resp_obj, field, None))

        instance._resp = resp_obj
        return instance

    def _refresh(self, data: dict) -> None:
        """Refresh the fields of this instance from the given response dictionary"""
        # Deserialize the response
        resp_obj = ModelResp(**data)

        # Reset fields
        self.schema = resp_obj.schema_
        self.project_id = resp_obj.project.id

        fields = [
            'id',
            'name',
            'spec',
            'input_type',
            'task',
            'task_params',
            'description',
            'event_id_col',
            'event_ts_col',
            'event_ts_format',
            'xai_params',
            'created_at',
            'updated_at',
            'artifact_status',
            'artifact_files',
            'is_binary_ranking_model',
        ]
        for field in fields:
            setattr(self, field, getattr(resp_obj, field, None))

        self._resp = resp_obj

    @cached_property
    def _artifact(self) -> ModelArtifact:
        """Model artifact instance"""
        assert self.id is not None
        return ModelArtifact(model_id=self.id)

    @cached_property
    def _surrogate(self) -> Surrogate:
        """Model artifact instance"""
        assert self.id is not None
        return Surrogate(model_id=self.id)

    @cached_property
    def _event_publisher(self) -> EventPublisher:
        """Event publisher instance"""
        assert self.id is not None
        return EventPublisher(model_id=self.id)

    @classmethod
    @handle_api_error
    def get(cls, id_: UUID | str) -> Model:
        """Get the model instance using model id."""
        response = cls._client().get(url=cls._get_url(id_))
        return cls._from_response(response=response)

    @classmethod
    @handle_api_error
    def from_name(cls, name: str, project_name: str) -> Model:
        """Get the model instance using model name and project name."""
        _filter = QueryCondition(
            rules=[
                QueryRule(field='name', operator=OperatorType.EQUAL, value=name),
                QueryRule(
                    field='project_name',
                    operator=OperatorType.EQUAL,
                    value=project_name,
                ),
            ]
        )

        response = cls._client().get(
            url=cls._get_url(), params={'filter': _filter.json()}
        )

        if response.json()['data']['total'] == 0:
            raise_not_found('Model not found for the given identifier')

        return cls.get(id_=response.json()['data']['items'][0]['id'])

    @handle_api_error
    def create(self) -> Model:
        """Create a new model."""
        response = self._client().post(
            url=self._get_url(),
            data={
                'name': self.name,
                'project_id': str(self.project_id),
                'schema': self.schema.dict(),
                'spec': self.spec.dict(),
                'input_type': self.input_type,
                'task': self.task,
                'task_params': self.task_params.dict(),
                'description': self.description,
                'event_id_col': self.event_id_col,
                'event_ts_col': self.event_ts_col,
                'event_ts_format': self.event_ts_format,
                'xai_params': self.xai_params.dict(),
            },
        )
        self._refresh_from_response(response=response)
        return self

    @handle_api_error
    def update(self) -> None:
        """Update an existing model."""
        body: dict[str, Any] = {
            'xai_params': self.xai_params.dict(),
            'description': self.description,
            'event_id_col': self.event_id_col,
            'event_ts_col': self.event_ts_col,
            'event_ts_format': self.event_ts_format,
        }

        response = self._client().patch(url=self._get_url(id_=self.id), data=body)
        self._refresh_from_response(response=response)

    @classmethod
    @handle_api_error
    def list(
        cls,
        project_id: UUID | None = None,
    ) -> Iterator[ModelCompact]:
        """
        Get a list of all models with the given filters

        :param project_id: Project identifier
        :return: ModelCompact iterator
        """
        params = {}
        if project_id:
            params['project_id'] = project_id

        for model in cls._paginate(url=cls._get_url(), params=params):
            yield ModelCompact(id=model['id'], name=model['name'])

    @property
    def datasets(self) -> Iterator[Dataset]:
        """Fetch all the datasets of this model"""
        from fiddler3.entities.dataset import (  # pylint: disable=import-outside-toplevel
            Dataset,
        )

        yield from Dataset.list(model_id=self.id)

    @property
    @handle_api_error
    def model_deployment(self) -> ModelDeployment:
        """Fetch all the deployments for this model"""
        assert self.id is not None

        return ModelDeployment.of(model_id=self.id)

    @classmethod
    @handle_api_error
    def generate_schema(
        cls,
        source: pd.DataFrame | Path | builtins.list[dict[str, Any]] | str,
        max_cardinality: int | None = None,
        sample_size: int | None = None,
        enrich: bool = True,
    ) -> ModelSchema:
        """
        Generate model schema from the given data.

        :param source: Data source - Dataframe or path to csv or parquet file.
        :param max_cardinality: Max cardinality to detect categorical columns.
        :param sample_size: No. of samples to use for generating schema.
        :param enrich: Enrich the model schema client side by scanning all data.
        :return: Generated ModelSchema object.
        """
        schema_generator = SchemaGeneratorFactory.create(
            source=source,
            max_cardinality=max_cardinality,
            sample_size=sample_size,
            enrich=enrich,
        )

        return schema_generator.generate(client=cls._client())

    @handle_api_error
    def delete(self) -> Job:
        """Delete a model and it's associated resources."""
        assert self.id is not None
        response = self._client().delete(url=self._get_url(id_=self.id))

        job_compact = JobCompactResp(**response.json()['data']['job'])
        return Job.get(id_=job_compact.id)

    @handle_api_error
    def publish(
        self,
        source: builtins.list[dict[str, Any]] | str | Path | pd.DataFrame,
        environment: EnvType = EnvType.PRODUCTION,
        dataset_name: str | None = None,
        update: bool = False,
    ) -> builtins.list[UUID] | Job:
        """
        Publish Pre-production or Production data

        :param source: one of:
            Path or str path: path for data file.
            list[dict]: list of events (max 1000) PRE_PRODUCTION environment is not
                supported
            dataframe: events dataframe. EnvType.PRE_PRODUCTION not supported.
        :param environment: Either EnvType.PRE_PRODUCTION or EnvType.PRODUCTION
        :param dataset_name: Name of the dataset. Not supported for EnvType.PRODUCTION
        :param update: flag indicating if the events are updates to previously
            published rows

        :return: list[UUID] for list of dicts or dataframe source and Job object for
            file path source.
        """

        return self._event_publisher.publish(
            source=source,
            environment=environment,
            dataset_name=dataset_name,
            update=update,
        )

    def add_artifact(
        self,
        model_dir: str | Path,
        deployment_params: DeploymentParams | None = None,
    ) -> Job:
        """
        Upload and deploy model artifact.

        :param model_dir: Path to model artifact tar file
        :param deployment_params: Model deployment parameters
        :return: Async job instance
        """
        return self._artifact.add(
            model_dir=model_dir, deployment_params=deployment_params
        )

    def update_artifact(
        self,
        model_dir: str | Path,
        deployment_params: DeploymentParams | None = None,
    ) -> Job:
        """
        Update existing model artifact.

        :param model_dir: Path to model artifact tar file
        :param deployment_params: Model deployment parameters
        :return: Async job instance
        """
        return self._artifact.update(
            model_dir=model_dir, deployment_params=deployment_params
        )

    def download_artifact(
        self,
        output_dir: str | Path,
    ) -> None:
        """
        Download existing model artifact.

        :param output_dir: Path to download model artifact tar file
        """

        self._artifact.download(output_dir=output_dir)

    def add_surrogate(
        self,
        deployment_params: DeploymentParams | None = None,
    ) -> Job:
        """
        Add a new surrogate model

        :param deployment_params: Model deployment parameters
        :return: Async job
        """
        job = self._surrogate.add(deployment_params=deployment_params)
        return job

    @handle_api_error
    def update_surrogate(
        self,
        deployment_params: DeploymentParams | None = None,
    ) -> Job:
        """
        Update an existing surrogate model

        :param deployment_params: Model deployment parameters
        :return: Async job
        """
        job = self._surrogate.update(deployment_params=deployment_params)
        return job


@dataclass
class ModelCompact:
    id: UUID
    name: str

    def fetch(self) -> Model:
        """Fetch model instance"""
        return Model.get(id_=self.id)


class ModelCompactMixin:
    @property
    def model(self) -> ModelCompact:
        """Model instance"""
        response = getattr(self, '_resp', None)
        if not response or not hasattr(response, 'model'):
            raise AttributeError(
                'This property is available only for objects generated from API '
                'response.'
            )

        return ModelCompact(id=response.model.id, name=response.model.name)
