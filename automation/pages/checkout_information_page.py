from core.pages.base_page import BasePage


class CheckoutInformationPage(BasePage):
    PAGE_TITLE = '[data-test="title"]'
    FIRST_NAME_INPUT = '[data-test="firstName"]'
    LAST_NAME_INPUT = '[data-test="lastName"]'
    POSTAL_CODE_INPUT = '[data-test="postalCode"]'
    CONTINUE_BUTTON = '[data-test="continue"]'

    def should_be_on_checkout_information_page(self) -> None:
        self.assert_contains_text(self.PAGE_TITLE, "Checkout: Your Information")
        self.assert_url_contains("/checkout-step-one.html")
        self.takeScreenshot("Checkout information page displayed")

    def fill_first_name(self, first_name: str) -> None:
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.takeScreenshot(f"First name filled with {first_name}")

    def fill_last_name(self, last_name: str) -> None:
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.takeScreenshot(f"Last name filled with {last_name}")

    def fill_postal_code(self, postal_code: str) -> None:
        self.fill(self.POSTAL_CODE_INPUT, postal_code)
        self.takeScreenshot(f"Postal code filled with {postal_code}")

    def continue_checkout(self) -> None:
        self.takeScreenshot("Continuing checkout information")
        self.click(self.CONTINUE_BUTTON)
