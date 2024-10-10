from behave import *
from behave.log_capture import LoggingCapture
from loguru import logger
# from test.ConfigFileReader import ConfigFileReader


@given(u'I run application')
def step_impl(context):
    logger.debug("Hello debug log")
    logger.info("Hello info log")
    print("Hello from steps file")
    # logger.error("My error")
    # ConfigFileReader.readConfigFile(context)

