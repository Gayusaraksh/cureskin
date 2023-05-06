from pages.base_page import Page
from selenium.webdriver.common.by import By


class Header(Page):
    SHOP_BY_CATEGORY_LINK = (By.XPATH,"//span[@class='label'][text()='Shop by Category']")
    FACE_LINK = (By.XPATH,"//span[@class='label'][text()='Face']")
    CLICK_SEARCH = (By.XPATH,'//search-modal[@class="header__search"]')
    SEARCH_TEXT = (By.CSS_SELECTOR,'input#Search-In-Modal')
    CLICK_PRODUCT_SEARCH = (By.CSS_SELECTOR,'button[type="submit"][class="search__button focus-inset"]')
    FACE_FOAM = (By.XPATH,'//a[contains(@href,"gentle-cleanse-face-foam")]')
    ADD_TO_CART_ICON = (By.CSS_SELECTOR,'span#cart-icon-bubble')

    def click_shop_by_category(self):
        self.click(*self.SHOP_BY_CATEGORY_LINK)

    def click_face(self):
        self.click(*self.FACE_LINK)

    def click_search(self):
        self.click(*self.CLICK_SEARCH)

    def enter_search_text(self,exp_text):
        self.input_text(exp_text,*self.SEARCH_TEXT)

    def click_product_search(self):
        self.click(*self.CLICK_PRODUCT_SEARCH)

    def click_first_product(self):
        self.click(*self.FACE_FOAM)

    def click_cart_icon(self):
        self.click(*self.ADD_TO_CART_ICON)

