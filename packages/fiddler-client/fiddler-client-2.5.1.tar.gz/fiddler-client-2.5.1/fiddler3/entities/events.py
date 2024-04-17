from __future__ import annotations

from pathlib import Path
from typing import Any, Iterator
from uuid import UUID

import pandas as pd
from requests import Response

from fiddler3.configs import STREAM_EVENT_LIMIT
from fiddler3.connection import ConnectionMixin
from fiddler3.decorators import handle_api_error
from fiddler3.entities.file import File
from fiddler3.entities.job import Job
from fiddler3.schemas.dataset import EnvType
from fiddler3.schemas.events import EventsSource, FileSource
from fiddler3.schemas.job import JobCompactResp


class EventPublisher(ConnectionMixin):
    STREAM_LIMIT = STREAM_EVENT_LIMIT

    def __init__(self, model_id: UUID) -> None:
        """
        Event publishing methods

        :param model_id: Model identifier
        """
        self.model_id = model_id

    def _get_stream_chunks(
        self, source: pd.DataFrame | list[dict[str, Any]]
    ) -> Iterator[list[dict[str, Any]]]:
        """Chunk the source based on stream limit"""

        for i in range(0, len(source), self.STREAM_LIMIT):
            chunk = source[i : i + self.STREAM_LIMIT]

            if isinstance(chunk, pd.DataFrame):
                events = chunk.to_dict('records')
            else:
                events = chunk

            yield events

    @handle_api_error
    def publish(
        self,
        source: list[dict[str, Any]] | str | Path | pd.DataFrame,
        environment: EnvType = EnvType.PRODUCTION,
        dataset_name: str | None = None,
        update: bool = False,
    ) -> list[UUID] | Job:
        """
        Publish Pre-production or Production data

        :param source: one of:
            Path or str path: path for data file.
            list[dict]: list of event dicts (max 1000) EnvType.PRE_PRODUCTION is not supported
            dataframe: events dataframe. EnvType.PRE_PRODUCTION not supported.
        :param environment: Either EnvType.PRE_PRODUCTION or EnvType.PRODUCTION
        :param dataset_name: Name of the dataset. Not supported for EnvType.PRODUCTION
        :param update: flag indicating if the events are updates to previously published rows

        :return: list[UUID] for list of dicts or dataframe source and Job object for file path source.
        """
        if isinstance(source, (str, Path)):
            return self._publish_file(
                source=source,
                environment=environment,
                dataset_name=dataset_name,
                update=update,
            )

        if isinstance(source, (list, pd.DataFrame)):
            return self._publish_stream(source=source, update=update)

        raise ValueError(f'Unsupported source - {type(source)}')

    def _publish_stream(
        self,
        source: list[dict[str, Any]] | pd.DataFrame,
        update: bool = False,
    ) -> list[UUID]:
        fiddler_ids = []
        for events in self._get_stream_chunks(source=source):
            response = self._publish_call(
                source=EventsSource(events=events),
                environment=EnvType.PRODUCTION,
                dataset_name=None,
                update=update,
            )
            fiddler_ids.extend(response.json()['data']['fiddler_ids'])

        return fiddler_ids

    def _publish_file(
        self,
        source: Path | str,
        environment: EnvType,
        dataset_name: str | None = None,
        update: bool = False,
    ) -> Job:
        file = File(path=Path(source)).upload()

        assert file.id is not None

        response = self._publish_call(
            source=FileSource(file_id=file.id),
            environment=environment,
            dataset_name=dataset_name,
            update=update,
        )
        job_compact = JobCompactResp(**response.json()['data']['job'])
        return Job.get(id_=job_compact.id)

    def _publish_call(
        self,
        source: FileSource | EventsSource,
        environment: EnvType,
        dataset_name: str | None = None,
        update: bool = False,
    ) -> Response:
        if update:
            method = self._client().patch
        else:
            method = self._client().post
        return method(
            url='/v3/events',
            data={
                'source': source.dict(),
                'model_id': self.model_id,
                'env_type': environment,
                'env_name': dataset_name,
            },
        )
