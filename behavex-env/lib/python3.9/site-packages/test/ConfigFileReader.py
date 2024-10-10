from jproperties import Properties
# from test.crypto_config.cryptoconfigparser import CryptoConfigParser, ParsingError
# from test.crypto_config.crypt import Crypt
# from test.crypto_config.demok import hello1
import os
# from cryptography.fernet import Fernet
# from cryptography.fernet import Fernet

class ConfigFileReader():
    browser_name = None
    browser_headless = None
    browser_startMaximized = None
    browser_incognito = None
    browser_binary = None
    website = None
    webdriver_path = None
    # with open('test\\qa\\application.properties', 'rb') as config_file:
    # with open(os.path.curdir+'\\'+ +'\\application.properties', 'rb') as config_file:
    #     configs.load(config_file)

        # f = Fernet(b'RQP-jvtG_ncu2rl2iJs7ZuIZ4DmBPzfpsMf45qBgEik=')
    

    def readConfigFile(context):
        configs = Properties()
        print(context)
        # with open(os.path.dirname(__file__)+'\\'+ context.config.userdata.get('profile') +'\\application.properties', 'rb') as config_file:
        with open(os.path.dirname(__file__)+'\\'+ context +'\\application.properties', 'rb') as config_file:
            print(os.path.curdir) 
            print(context)
            configs.load(config_file)
            
        # try:
        #     properties = CryptoConfigParser(crypt_key=key)
        # except ParsingError as err:
        #     print('Could not parse:', err)
        # print(Crypt(Crypt.gen_key()).encrypt('demokk'))
        # hello1()

        print(configs["browser.name"].data)
        print(configs["name"].data)
        ConfigFileReader.browser_name = configs["browser.name"].data
        ConfigFileReader.browser_headless = configs["browser.headless"].data
        ConfigFileReader.browser_startMaximized = configs["browser.startMaximized"].data
        ConfigFileReader.browser_incognito = configs["browser.incognito"].data
        ConfigFileReader.browser_binary = configs["browser.binary"].data
        ConfigFileReader.website = configs["url"].data
        ConfigFileReader.webdriver_path = configs["webdriver.path"].data
        print(ConfigFileReader.webdriver_path)
        # s = configs["name"].data
        # try:
        #     encrypted_str = s.encode()
        # except AttributeError:
        #     encrypted_str = s

        # decrypted = key.decrypt(encrypted_str)
        # print(decrypted.decode())
        # properties.read(config_file)
        # print(properties.get('User', 'name'))
        # print(f.encrypt(configs["name1"].data))
    
