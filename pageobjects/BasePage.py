from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    
    def __init__(self, driver):
        print("Inside base page")
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def timeout(self, duration):
         WebDriverWait(self.driver, duration)

    def waitToDisappear(self, element):
         element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(element))
         return bool(element)

    def click(self, by_locator):
        """
        Clicking on a specific element, if element not found within timeout then error thrown

        :Args:
            - by_locator - locator of the element to be clicked
        """
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        element.location_once_scrolled_into_view
        element.click()

    def clickme(self, element):
        element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(element))
        element.location_once_scrolled_into_view
        element.click()
    
    def assert_element_text(self, by_locator, element_text):
        """
        compare the element text with the given text

        :Args:
         - by_locator - locator of the element in which text value will taken
         - element_text - compare text
        """
        web_element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool (web_element.get_attribute('textContent') == element_text)

    def enter_text(self, by_locator, text):
        """
        entering a text on a specific web element

        :Args:
         - by_locator - locator of the element in which text will be entered
         - text - text to be entered in the field
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_visible(self,by_locator):
        """
        checking the visiblity of a specific element 

        :Args:
         - by_locator - locator value to be identified.
        """
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_enable(self,by_locator):
        """
        checking the enable status of a specific element 

        :Args:
         - by_locator - locator value to be identified.
        """
        element=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator))
        return bool(element)

    def is_disable(self,by_locator):
        """
        checking the disable status of a specific element 

        :Args:
         - by_locator - locator value to be identified.
        """
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute('disabled')

    def get_property(self, by_locator, property):
        """
        get the property of a specific element 

        :Args:
         - by_locator - locator value to be identified.
         - property - proerty name to be identified
        """
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(property)

    def get_element(self, by_locator):
        """
        get a specific element

        :Args:
         - by_locator - locator value to be identified.
        """
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def is_invisible(self,by_locator):
        """
        checking the invisiblity of a specific element 

        :Args:
         - by_locator - locator value to be identified.
        """
        element=WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(by_locator))
        return element.value_of_css_property('display')
    
    def find_elements_by_xpath(self,*by_locator):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.find_elements(*by_locator)
    
    def wait1(self):
        self.driver.implicitly_wait(10)

    def selectFromDropdownByValue(self, by_locator, value):
        self.wait1()
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.location_once_scrolled_into_view
        element1 = Select(element)
        element1.select_by_value(value)

    def selectFromDropdownByIndex(self, by_locator, index):
        self.wait1()
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.location_once_scrolled_into_view
        element1 = Select(element)
        element1.select_by_index(index)