from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    MINUS_BUTTON = (By.XPATH,'//button[@name="minus"]')
    CART_EMPTY = (By.CSS_SELECTOR,'h3.mini-cart__empty-text')

    def click_minus_button(self):
        self.click(*self.MINUS_BUTTON)

    def cart_empty(self,exp_text):
        self.verify_text(exp_text,*self.CART_EMPTY)