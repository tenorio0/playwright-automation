from playwright_core.pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    PAGE_TITLE = '[data-test="title"]'
    SUMMARY_CONTAINER = '[data-test="checkout-summary-container"]'
    FINISH_BUTTON = '[data-test="finish"]'

    def should_be_on_checkout_overview_page(self) -> None:
        self.assert_contains_text(self.PAGE_TITLE, "Checkout: Overview")
        self.assert_url_contains("/checkout-step-two.html")
        self.takeScreenshot("Checkout overview page displayed")

    def should_contain_product(self, product_name: str) -> None:
        self.assert_contains_text(self.SUMMARY_CONTAINER, product_name)
        self.takeScreenshot(f"Checkout overview contains product -> {product_name}")

    def click_finish(self) -> None:
        self.takeScreenshot("Finishing checkout")
        self.click(self.FINISH_BUTTON)
