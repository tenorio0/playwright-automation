from core.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '[data-test="error"]'

    def open(self) -> None:
        self.navigate_to()
        self.wait_for_visibility(self.USERNAME_INPUT)
        self.takeScreenshot("Login page loaded")

    def enter_username(self, username: str) -> None:
        self.fill(self.USERNAME_INPUT, username)
        self.takeScreenshot(f"Username filled with {username}")

    def enter_password(self, password: str) -> None:
        self.fill(self.PASSWORD_INPUT, password)
        masked_password = "*" * len(password)
        self.takeScreenshot(f"Password filled with {masked_password}")

    def click_login(self) -> None:
        self.takeScreenshot("Clicking on -> Login button")
        self.click(self.LOGIN_BUTTON)

    def should_show_error_message(self, expected_message: str) -> None:
        self.assert_contains_text(self.ERROR_MESSAGE, expected_message)
        self.takeScreenshot("Login error message displayed")
