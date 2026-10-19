from pages.base_page import BasePage


class HomePage(BasePage):

    PRODUCTS_TITLE = ".title"

    def verify_home_page(self):
        return self.is_visible(self.PRODUCTS_TITLE)
