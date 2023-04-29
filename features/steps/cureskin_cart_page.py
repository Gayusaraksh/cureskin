import time

from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on - button to reduce product quantity')
def click_minus_button(context):
    context.app.cart_page.click_minus_button()
    time.sleep(2)


@then('Verify that {exp_text} message is displayed')
def cart_empty(context,exp_text):
    context.app.cart_page.cart_empty(exp_text)