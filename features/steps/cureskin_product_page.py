from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click add to cart button')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()