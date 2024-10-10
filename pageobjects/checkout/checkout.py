from selenium.webdriver.common.by import By
from pageobjects.BasePage import BasePage
import time

class checkout(BasePage):
    
    country = (By.XPATH, "//*[@id='BillingNewAddress_CountryId']")
    province = (By.XPATH, "//*[@id='BillingNewAddress_StateProvinceId']")
    city = (By.XPATH, "//*[@id='BillingNewAddress_City']")
    address1 = (By.XPATH, "//*[@id='BillingNewAddress_Address1']")
    postalCode = (By.XPATH, "//*[@id='BillingNewAddress_ZipPostalCode']")
    phoneNumber = (By.XPATH, "//*[@id='BillingNewAddress_PhoneNumber']")
    billingAddressButton = (By.XPATH, "//*[@id='billing-buttons-container']/input[@title='Continue']")
    billingAddressSelect = (By.XPATH, "//*[@id='billing-address-select']")
    shippingAddressSelect = (By.XPATH, "//*[@id='shipping-address-select']")
    shippingAddressButton = (By.XPATH, "//*[@id='shipping-buttons-container']/input[@title='Continue']")
    shippingMethod = (By.XPATH, "//li[@id='opc-shipping_method']/descendant::li")
    shippingMethodButton = (By.XPATH, "//div[@id='shipping-method-buttons-container']/input[@value='Continue']")
    paymentMethodButton = (By.XPATH, "//div[@id='payment-method-buttons-container']/input[@value='Continue']")
    paymentInformationButton = (By.XPATH, "//div[@id='payment-info-buttons-container']/input[@value='Continue']")
    confirmOrderButton = (By.XPATH, "//div[@id='confirm-order-buttons-container']/input[@value='Confirm']")


    def enterBillingDetails(self):
        if self.is_visible(self.billingAddressSelect) == True:
            self.selectFromDropdownByIndex(self.billingAddressSelect, 0)
            self.clickme(self.billingAddressButton)
        else:
            self.selectFromDropdownByValue(self.country, "2")
            self.selectFromDropdownByValue(self.province, "71")
            self.enter_text(self.city, "Scarborough")
            self.enter_text(self.address1, "123 demo road")
            self.enter_text(self.postalCode, "123 456")
            self.enter_text(self.phoneNumber, "123456789")
            self.clickme(self.billingAddressButton)
            

    def enterShippingDetails(self):
        self.selectFromDropdownByIndex(self.shippingAddressSelect, 0)
        self.clickme(self.shippingAddressButton)
        

    def enterShippingMethod(self, mode):
        ship = "//li[@id='opc-shipping_method']/descendant::li"
        if mode == "Ground":
            shippingMethodComplete = ship+"/descendant::label[contains(text(), '" + mode + "')]"
            shippingMethodComplete1 = (By.XPATH, shippingMethodComplete)
            self.clickme(shippingMethodComplete1)
            self.clickme(self.shippingMethodButton)
        elif mode == "Next Day":
            shippingMethodComplete = ship+"/descendant::label[contains(text(), '" + mode + "')]"
            shippingMethodComplete1 = (By.XPATH, shippingMethodComplete)
            self.clickme(shippingMethodComplete1)
            self.clickme(self.shippingMethodButton)
        elif mode == "2nd Day":
            shippingMethodComplete = ship+"/descendant::label[contains(text(), '" + mode + "')]"
            shippingMethodComplete1 = (By.XPATH, shippingMethodComplete)
            self.clickme(shippingMethodComplete1)
            self.clickme(self.shippingMethodButton)

    def enterPaymentMethod(self, mode):
        payment = "//li[@id='opc-payment_method']/descendant::li"
        if mode == "Cash On Delivery":
            paymentComplete = payment+"/descendant::label[contains(text(), '" + mode + "')]"
            paymentComplete1 = (By.XPATH, paymentComplete)
            self.clickme(paymentComplete1)
            self.clickme(self.paymentMethodButton)
        elif mode == "Check/Money Order":
            paymentComplete = payment+"/descendant::label[contains(text(), '" + mode + "')]"
            paymentComplete1 = (By.XPATH, paymentComplete)
            self.clickme(paymentComplete1)
            self.clickme(self.paymentMethodButton)
        elif mode == "Credit Card":
            paymentComplete = payment+"/descendant::label[contains(text(), '" + mode + "')]"
            paymentComplete1 = (By.XPATH, paymentComplete)
            self.clickme(paymentComplete1)
            self.clickme(self.paymentMethodButton)
        elif mode == "Purchase Order":
           paymentComplete = payment+"/descendant::label[contains(text(), '" + mode + "')]"
           paymentComplete1 = (By.XPATH, paymentComplete)
           self.clickme(paymentComplete1)
           self.clickme(self.paymentMethodButton)

    def enterPaymentInformation(self):
        self.clickme(self.paymentInformationButton)

    def orderConfirmation(self):
        self.clickme(self.confirmOrderButton)

    # def billingContinue(self):
        