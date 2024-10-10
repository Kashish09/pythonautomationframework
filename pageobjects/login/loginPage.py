from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage

class login(BasePage):

    def __init__(self, driver):
        self.driver = driver
        

    EMAIL_ID = (By.XPATH, "//*[@id='Email']")
    PASSWORD = (By.XPATH, "//*[@id='Password']")
    LOGIN_BUTTON = (By.XPATH,"//*[@type='submit' and @value='Log in']")

    def set_email(self, username):
        self.enter_text(self.EMAIL_ID, username)

    def set_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_sign_in_btn(self):
        self.click(self.LOGIN_BUTTON)

    # def is_failure_message_displayed(self):
    #     failure_message_element = self.driver.find_element(*LoginPage.failure_message)
    #     return failure_message_element.is_displayed()

    def login(self, username, password):
        self.set_email(username)
        self.set_password(password)
        self.click_sign_in_btn()