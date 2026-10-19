from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def enter_text(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()