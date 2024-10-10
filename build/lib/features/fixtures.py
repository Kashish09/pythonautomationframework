import logging
from behave import fixture
from loguru import logger


@fixture
def log_capture_fix(context):
    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)
    logger.remove()
    handler_id = logger.add(PropogateHandler(), format="{message}")
    yield context.log_capture
    logger.remove(handler_id)