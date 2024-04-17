import logging

from fiddler3.constants.common import LOGGER_NAME
from fiddler3.utils.logger import set_logging


def test_set_logging() -> None:
    app_logger = logging.getLogger(LOGGER_NAME)
    assert len(app_logger.handlers) == 0

    set_logging(level=logging.ERROR)
    assert len(app_logger.handlers) == 1
