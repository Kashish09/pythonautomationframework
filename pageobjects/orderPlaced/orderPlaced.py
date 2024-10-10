from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage
import re

class orderPlaced(BasePage):

    continueButton = (By.XPATH, "//div[@class='buttons']/descendant::input[@value='Continue']")
    orderNumber = (By.XPATH, "//div[@class='section order-completed']/descendant::ul[@class='details']/li[contains(text(), 'Order')]")
    orderDetailsLink = (By.XPATH, "//div[@class='section order-completed']/descendant::ul[@class='details']/descendant::a[contains(text(), 'Click here for order details')]")


    def retrieveOrderNumber(self):
        orderNumberElement = self.get_element(self.orderNumber)
        print(orderNumberElement.text)
        number = re.search(r'\d+', orderNumberElement.text)
        number1 = number.group()
        print(number1)
        return number1
    
    def downloadInvoice(self):
        self.clickme(self.orderDetailsLink)