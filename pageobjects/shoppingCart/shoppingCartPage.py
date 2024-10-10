from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage
import time

class shoppingCartPage(BasePage):

    cart = (By.XPATH, "//span[contains(text(), 'Shopping cart')]")
    productAddedNotification = (By.XPATH, "//div[@id='bar-notification']")
    serviceTerms = (By.XPATH, "//*[@id='termsofservice']")
    checkoutButton = (By.XPATH, "//*[@id='checkout' and contains(text(), 'Checkout')]")

    def goToCart(self):
        notification_bar = self.is_invisible(self.productAddedNotification)
        while notification_bar == 'block':
            self.wait1()
            notification_bar = self.is_invisible(self.productAddedNotification)
        self.click(self.cart)

    def checkout(self):
        self.clickme(self.serviceTerms)
        self.clickme(self.checkoutButton)