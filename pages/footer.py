from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class Footer(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR,'input#ContactFooter-email')
    CLICK_ARROW = (By.CSS_SELECTOR,'button[type="submit"][aria-label="Subscribe"]')
    SUCCESS_MSG = (By.CSS_SELECTOR,'h3[class="form__message"][id="ContactFooter-success"]')

    def enter_invalid_email(self,expected_text):
        self.input_text(expected_text,*self.EMAIL_FIELD)

    def click_arrow(self):
        self.click(*self.CLICK_ARROW)

    def verify_subscription_message(self,exp_text):
        self.verify_text(exp_text,*self.SUCCESS_MSG)
