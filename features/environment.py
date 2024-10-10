from behave import fixture
from behave import use_fixture
from features.fixtures import log_capture_fix
from loguru import logger
from test.helper import *
import os
import datetime


def before_all(context):
  context.driver = None
  context.featureTag = None
  use_fixture(log_capture_fix, context)
  context.config.setup_logging()

def before_feature(context, feature):
  logger.debug("Starting feature " + str(feature.name))
  logger.debug("Starting feature tags" + str(feature.tags))
  context.featureTag = feature.tags[0]

def before_scenario(context, scenario):
  logger.debug("Starting scenario " + str(scenario.name))
  logger.debug("Starting scenario tags " + str(scenario.tags))
  if "customdownloadfolder" in scenario.tags:
    folderName = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "-" + context.featureTag
    context.folderName = folderName
    os.makedirs(os.path.join("C:\\pythonautomationframework\\download", context.folderName))
  profile = context.config.userdata.get('profile')
  context.driver = helper.create_driver(profile, context.folderName)
  context.driver.get(ConfigFileReader.website)
  # os.makedirs(os.path.join(ConfigFileReader.download_path, context.folderName))
  
def after_scenario(context, scenario):
  if context.driver:
    if scenario.status == 'failed':
      DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
      context.driver.save_screenshot("screenshots/%s.png"%DateString)
    else:
      context.driver.quit()
      context.driver = None
      logger.debug("Finishing scenario " + str(scenario.name))
      logger.debug("Releasing driver")
  else:
    pass

def after_feature(context, feature):
  logger.debug("Finishing feature " + str(feature.name))