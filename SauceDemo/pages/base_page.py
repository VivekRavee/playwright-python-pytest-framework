from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    # =====================================================
    # Element Actions
    # =====================================================

    def click(self, locator):
        self.page.locator(locator).click()

    def double_click(self, locator):
        self.page.locator(locator).dblclick()

    def hover(self, locator):
        self.page.locator(locator).hover()

    def enter_text(self, locator, value):
        self.page.locator(locator).fill(value)

    def clear_text(self, locator):
        self.page.locator(locator).clear()

    def press_key(self, locator, key):
        self.page.locator(locator).press(key)

    # =====================================================
    # Dropdowns
    # =====================================================

    def select_by_value(self, locator, value):
        self.page.locator(locator).select_option(value=value)

    def select_by_label(self, locator, label):
        self.page.locator(locator).select_option(label=label)

    def select_by_index(self, locator, index):
        self.page.locator(locator).select_option(index=index)

    # =====================================================
    # Checkboxes & Radio Buttons
    # =====================================================

    def check(self, locator):
        self.page.locator(locator).check()

    def uncheck(self, locator):
        self.page.locator(locator).uncheck()

    def is_checked(self, locator):
        return self.page.locator(locator).is_checked()

    # =====================================================
    # File Operations
    # =====================================================

    def upload_file(self, locator, file_path):
        self.page.locator(locator).set_input_files(file_path)

    # =====================================================
    # Getters
    # =====================================================

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def get_value(self, locator):
        return self.page.locator(locator).input_value()

    def get_attribute(self, locator, attribute):
        return self.page.locator(locator).get_attribute(attribute)

    # =====================================================
    # Visibility & State
    # =====================================================

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def is_enabled(self, locator):
        return self.page.locator(locator).is_enabled()

    def is_disabled(self, locator):
        return self.page.locator(locator).is_disabled()

    # =====================================================
    # Wait Methods
    # =====================================================

    def wait_for_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def wait_for_hidden(self, locator):
        expect(self.page.locator(locator)).to_be_hidden()

    def wait_for_enabled(self, locator):
        expect(self.page.locator(locator)).to_be_enabled()

    # =====================================================
    # Assertion Methods
    # =====================================================

    def verify_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()
        

    def verify_hidden(self, locator):
        expect(self.page.locator(locator)).to_be_hidden()

    def verify_text(self, locator, expected_text):
        expect(self.page.locator(locator)).to_have_text(expected_text)

    def verify_contains_text(self, locator, expected_text):
        expect(self.page.locator(locator)).to_contain_text(expected_text)

    def verify_url_contains(self, expected_text):
        assert expected_text in self.page.url

    # =====================================================
    # Browser Utilities
    # =====================================================

    def get_current_url(self):
        return self.page.url

    def get_page_title(self):
        return self.page.title()

    def refresh_page(self):
        self.page.reload()

    def go_back(self):
        self.page.go_back()

    def go_forward(self):
        self.page.go_forward()
