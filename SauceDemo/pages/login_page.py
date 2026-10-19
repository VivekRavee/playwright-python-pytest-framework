from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"

    def enter_username(self, username):
        self.enter_text(
            self.USERNAME,
            username
        )

    def enter_password(self, password):
        self.enter_text(
            self.PASSWORD,
            password
        )

    def click_login(self):
        self.click(
            self.LOGIN_BTN
        )

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_login_success(self):
        return (
            "inventory.html"
            in self.page.url
        )