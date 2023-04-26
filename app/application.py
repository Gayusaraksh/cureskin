from pages.shop_page import ShopPage
from pages.header import Header
from pages.face_page import FacePage

class Application:

    def __init__(self,driver):
        self.driver = driver
        self.shop_page = ShopPage(self.driver)
        self.header = Header(self.driver)
        self.face_page = FacePage(self.driver)
