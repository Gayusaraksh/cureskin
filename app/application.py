from pages.shop_page import ShopPage
from pages.header import Header
from pages.face_page import FacePage
from pages.footer import Footer
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class Application:

    def __init__(self,driver):
        self.driver = driver
        self.shop_page = ShopPage(self.driver)
        self.header = Header(self.driver)
        self.face_page = FacePage(self.driver)
        self.footer = Footer(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)
