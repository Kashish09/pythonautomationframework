from behave import fixture
from behave import use_fixture
from features.fixtures import log_capture_fix
from loguru import logger
from test.helper import *
import datetime

def before_all(context):
  context.driver = None
  use_fixture(log_capture_fix, context)
  context.config.setup_logging()

def before_feature(context, feature):
  logger.debug("Starting feature " + str(feature.name))

def before_scenario(context, scenario):
  logger.debug("Starting scenario " + str(scenario.name))
  profile = context.config.userdata.get('profile')
  context.driver = helper.create_driver(profile)
  context.driver.get(ConfigFileReader.website)
  
def after_scenario(context, scenario):
  if context.driver:
    if scenario.status == 'failed':
      context.driver.save_screenshot("screenshots/" + datetime.datetime.now() + ".png")
    else:
      context.driver.quit()
      context.driver = None
      logger.debug("Finishing scenario " + str(scenario.name))
      logger.debug("Releasing driver")
  else:
    pass

def after_feature(context, feature):
  logger.debug("Finishing feature " + str(feature.name))