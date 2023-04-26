import time

from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Cureskin shop page')
def open_cureskin_shop(context):
    context.app.shop_page.open_cureskin_shop()
    time.sleep(5)
    whandle=context.driver.window_handles[0]
    context.driver.switch_to.window(whandle)
    # (context.driver.find_element(By.XPATH,'//div[@class="popup__content-wrapper"]'))
    time.sleep(2)
    context.driver.find_element(By.XPATH,'//button[@class="popup-close" and @type="button"]').click()


@when('Click on shop by category')
def click_shop_by_category(context):
    context.app.header.click_shop_by_category()
    time.sleep(2)


@when('Click on face option')
def click_face(context):
    context.app.header.click_face()

