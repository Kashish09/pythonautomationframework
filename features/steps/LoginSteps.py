from behave import *
from behave.log_capture import LoggingCapture
from loguru import logger
from test.helper import helper
from pageobjects.login import loginPage
from pageobjects.books import books
from pageobjects.shoppingCart import shoppingCartPage
from pageobjects.checkout import checkout
from pageobjects.orderPlaced import orderPlaced
from test.ConfigFileReader import ConfigFileReader
from pageobjects.orderDetails import orderDetails


@given(u'I open DemoWebShop Login page')
def step_impl(context):
    logger.debug("Opening DemoWenShop Login page")
    print(context.config.userdata.get('profile'))
    helper.openSite(context, "login")
    logger.debug("Entering login credentials")
    loginPage.login(context.driver).login(username = ConfigFileReader.username, password = ConfigFileReader.password)

@given(u'I go to books page')
def step_impl(context):
    logger.debug("Opening Books page")
    helper.openSite(context, "books")

@then(u'I add books to cart')
def step_impl(context):
    logger.debug("Adding books to cart")
    books.books(context.driver).addBooksToCart()
    logger.debug("Books added to cart")

@then(u'I go to cart and checkout')
def step_impl(context):
    logger.debug("Clicking cart button")
    shoppingCartPage.shoppingCartPage(context.driver).goToCart()
    logger.debug("Clicking checkout button on cart page")
    shoppingCartPage.shoppingCartPage(context.driver).checkout()

@then(u'I enter information on checkout page and confirm the Order')
def step_impl(context):
    logger.debug("On checkout page")
    checkout.checkout(context.driver).enterBillingDetails()
    checkout.checkout(context.driver).enterShippingDetails()
    checkout.checkout(context.driver).enterShippingMethod("Next Day")
    checkout.checkout(context.driver).enterPaymentMethod("Cash On Delivery")
    checkout.checkout(context.driver).enterPaymentInformation()
    logger.debug("Entered information on checkout page")
    checkout.checkout(context.driver).orderConfirmation()
    logger.debug("Clicked confirm order button")

@then(u'I see the order confirmation page and click on invoice link to go to invoice page')
def step_impl(context):
    logger.debug("On order confirmation page")
    orderNumber = orderPlaced.orderPlaced(context.driver).retrieveOrderNumber()
    print(orderNumber)
    logger.debug("Clicking on download invoice link")
    orderPlaced.orderPlaced(context.driver).downloadInvoice()

@then(u'I download invoice')
def step_impl(context):
    logger.debug("On invoice page")
    logger.debug("Clicking on download invoice page")
    orderDetails.orderDetails(context.driver).downloadPDFInvoice()