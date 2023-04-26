from pages.base_page import Page
from selenium.webdriver.common.by import By

class FacePage(Page):

    FACE_PROD_NAME = (By.CSS_SELECTOR,'a.card-information__text.h4[href="/collections/face/products/gentle-cleanse-face-foam"]')

    def verify_product_name(self,exp_result):
        self.verify_partial_text(exp_result,*self.FACE_PROD_NAME)

    def verify_header(self,expected_url):
        self.verify_current_url(expected_url)