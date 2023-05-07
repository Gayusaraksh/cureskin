import time

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Cureskin shop page')
def open_cureskin_shop(context):
    context.app.shop_page.open_cureskin_shop()
    time.sleep(5)
    whandle=context.driver.window_handles[0]
    context.driver.switch_to.window(whandle)
    # (context.driver.find_element(By.XPATH,'//div[@class="popup__content-wrapper"]'))
    time.sleep(10)
    context.driver.find_element(By.XPATH,'//button[@class="popup-close" and @type="button"]').click()


@when('Click on shop by category')
def click_shop_by_category(context):
    context.app.header.click_shop_by_category()
    time.sleep(2)


@when('Click on face option')
def click_face(context):
    context.app.header.click_face()


@when('Enter valid email id {expected_text}')
def enter_invalid_email(context,expected_text):
    context.app.footer.enter_invalid_email(expected_text)


@when('Click on arrow')
def click_arrow(context):
    context.app.footer.click_arrow()


@when('Click on search')
def click_search(context):
    context.app.header.click_search()


@when('Enter the product name {exp_text}')
def enter_search_text(context,exp_text):
    context.app.header.enter_search_text(exp_text)


@when('Click on product search button')
def click_product_search(context):
    context.app.header.click_product_search()


@when('Click the first item')
def click_first_product(context):
    context.app.header.click_first_product()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@then('Verify {exp_text} message is shown')
def verify_subscription_message(context,exp_text):
    context.app.footer.verify_subscription_message(exp_text)
