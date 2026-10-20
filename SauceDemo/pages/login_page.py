from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"

    def login_creds(self, username, password):
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
    def loginSubmit(self):
        self.click(self.LOGIN_BTN)

    def verify_login_success(self):
        self.verify_visible(".title")