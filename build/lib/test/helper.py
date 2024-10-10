from selenium import webdriver
from test.ConfigFileReader import ConfigFileReader

class helper():
    
  def create_driver(profile):
    
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

      if(bool(ConfigFileReader.browser_incognito)):
        chrome_options.add_argument("incognito")
      chrome_options.add_argument("start-maximized")
      chrome_options.add_argument("window-size=1900,1800")
      chrome_options.add_argument("--ignore-certificate-errors")
      # if(bool(ConfigFileReader.browser_headless)):
      #   chrome_options.add_argument("-headless")

      driver = webdriver.Chrome(executable_path=r'C:\\pythonautomationframework\\webdriver\\chromedriver' ,chrome_options=chrome_options)
      return driver
      # driver.get(ConfigFileReader.website)
    # pass
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.implicitly_wait(time_to_wait=10)
    # return driver
 