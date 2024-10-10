from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage

class books(BasePage):

    def __init__(self, driver):
        self.driver = driver

    bookList = (By.XPATH, "//*[@class='product-grid']/descendant::div[@class='item-box']")
    availableBooks = (By.XPATH, "//input[@type = 'button' and contains(@value, 'Add to cart')]")
    cartSuccess = (By.XPATH, "//div/p[contains(text(), 'The product has been added to your')]")


    def addBooksToCart(self):
        listOfBooks = self.find_elements_by_xpath(*self.availableBooks)
        for links in listOfBooks:
            print(links)
            self.clickme(links)
            self.is_visible(self.cartSuccess)