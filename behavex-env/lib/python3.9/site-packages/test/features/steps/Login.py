from behave import *
from test.ConfigFileReader import readQA


@Given("I run application")
def step_impl(context):
    print("Hello from steps file")
    readQA()