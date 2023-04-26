from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):
    SHOP_BY_CATEGORY_LINK = (By.XPATH,"//span[@class='label'][text()='Shop by Category']")
    FACE_LINK = (By.XPATH,"//span[@class='label'][text()='Face']")

    def click_shop_by_category(self):
        self.click(*self.SHOP_BY_CATEGORY_LINK)

    def click_face(self):
        self.click(*self.FACE_LINK)