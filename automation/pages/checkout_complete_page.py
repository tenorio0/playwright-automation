from playwright_core.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    PAGE_TITLE = '[data-test="title"]'
    COMPLETE_HEADER = '[data-test="complete-header"]'

    def should_show_order_success(self) -> None:
        self.assert_contains_text(self.PAGE_TITLE, "Checkout: Complete!")
        self.assert_contains_text(self.COMPLETE_HEADER, "Thank you for your order!")
        self.assert_url_contains("/checkout-complete.html")
        self.takeScreenshot("Checkout completed successfully")
