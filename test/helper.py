from selenium import webdriver
from test.ConfigFileReader import ConfigFileReader
import os
import time

class helper():

  def create_driver(profile, downloadFolder):
    
    print("profile helper "+profile)
    ConfigFileReader.readConfigFile(profile)
    print("browser_name " + ConfigFileReader.browser_name)
    if ConfigFileReader.browser_name == "chrome":
      chrome_options = webdriver.ChromeOptions()
      # chrome_options.add_argument("disable-infobars")
      chrome_options.add_argument("--test-type")
      chrome_options.add_argument("--no-sandbox")
      chrome_options.add_argument("--disable-gpu")
      chrome_options.add_argument("--disable-popup-blocking")
      chrome_options.add_argument("--disable-web-security")
      chrome_options.add_argument("--allow-running-insecure-content")
      chrome_options.add_argument("--remote-allow-origins=*")

      # if(bool(ConfigFileReader.browser_incognito)):
      #   chrome_options.add_argument("incognito")
      chrome_options.add_argument("start-maximized")
      chrome_options.add_argument("window-size=1900,1800")
      chrome_options.add_argument("--ignore-certificate-errors")
      prefs = {'download.default_directory' : os.path.join(ConfigFileReader.download_path, downloadFolder), 
               "download.prompt_for_download": False,
               "browser.enabled_labs_experiments": ['download-bubble@2', 'download-bubble-v2@2'],
               "download.manager.showWhenStarting": False,
               "download.directory_upgrade": True
               }
      chrome_options.add_experimental_option("prefs", prefs)
      chrome_options.add_argument("--browser.helperApps.neverAsk.saveToDisk=application/pdf")
      chrome_options.add_argument("disable-features=DownloadBubble,DownloadBubbleV2")
      # if(bool(ConfigFileReader.browser_headless)):
      #   chrome_options.add_argument("-headless")
      driver = webdriver.Chrome(executable_path=ConfigFileReader.webdriver_path ,chrome_options=chrome_options)
      return driver

  def openSite(context, extendedpath):
    print("Website inopenSite")
    print(ConfigFileReader.website + extendedpath)
    context.driver.get(ConfigFileReader.website + extendedpath)
    time.sleep(5)