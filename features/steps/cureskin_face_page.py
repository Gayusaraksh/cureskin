from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify {exp_result} is present in first product name')
def verify_product_name(context,exp_result):
    context.app.face_page.verify_product_name(exp_result)


@then('Verify {expected_url} header is shown')
def verify_header(context,expected_url):
    context.app.face_page.verify_header(expected_url)