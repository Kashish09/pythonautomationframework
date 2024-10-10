from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage
import re
import time

class orderDetails(BasePage):

    pdfInvoice = (By.XPATH, "//div[@class='page-title']/descendant::a[contains(text(), 'PDF Invoice')]")


    def downloadPDFInvoice(self):
        self.clickme(self.pdfInvoice)
        time.sleep(10)