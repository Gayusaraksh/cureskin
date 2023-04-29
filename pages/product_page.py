from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    ADD_TO_CART = (By.CSS_SELECTOR, 'button.product-form__submit.button.button--secondary.button--full-width')

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART)


