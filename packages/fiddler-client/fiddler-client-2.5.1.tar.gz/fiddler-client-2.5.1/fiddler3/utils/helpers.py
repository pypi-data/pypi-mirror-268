from __future__ import annotations

from datetime import datetime
from http import HTTPStatus

import pandas as pd

from fiddler3.constants.common import TIMESTAMP_FORMAT
from fiddler3.constants.model import DataType
from fiddler3.exceptions import NotFound
from fiddler3.schemas.response import ErrorData, ErrorItem
from fiddler3.utils.logger import get_logger

logger = get_logger(__name__)


def try_series_retype(series: pd.Series, new_type: str) -> pd.DataFrame | pd.Series:
    """Retype series."""
    if new_type in ['unknown', 'str']:
        # Do not retype data
        return series

    try:
        return series.astype(new_type)
    except (TypeError, ValueError) as e:
        if new_type == 'int':
            logger.warning(
                '"%s" cannot be loaded as int '
                '(likely because it contains missing values, and '
                'Pandas does not support NaN for ints). Loading '
                'as float instead.',
                series.name,
            )
            return series.astype('float')
        if new_type.lower() == DataType.TIMESTAMP.value:
            try:
                return series.apply(lambda x: datetime.strptime(x, TIMESTAMP_FORMAT))
            # if timestamp str doesn't contain millisec.
            except ValueError:
                # @TODO: Should such cases be
                # 1. handled by client OR
                # 2. should server apped 00 ms if not present during ingestion OR
                # 3. should it break if timestamp format does not match while ingestion?
                return series.apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
        else:
            raise e


def raise_not_found(message: str) -> None:
    """Raise NotFound if the resource is not found while fetching with names"""
    raise NotFound(
        error=ErrorData(
            code=HTTPStatus.NOT_FOUND,
            message=message,
            errors=[
                ErrorItem(
                    reason='ObjectNotFound',
                    message=message,
                    help='',
                ),
            ],
        ),
    )
