from playwright_core.pages.base_page import BasePage


class CartPage(BasePage):
    PAGE_TITLE = '[data-test="title"]'
    CART_LIST = '[data-test="cart-list"]'
    CHECKOUT_BUTTON = '[data-test="checkout"]'

    def should_be_on_cart_page(self) -> None:
        self.assert_contains_text(self.PAGE_TITLE, "Your Cart")
        self.assert_url_contains("/cart.html")
        self.takeScreenshot("Cart page displayed")

    def should_contain_product(self, product_name: str) -> None:
        self.assert_contains_text(self.CART_LIST, product_name)
        self.takeScreenshot(f"Cart contains product -> {product_name}")

    def click_checkout(self) -> None:
        self.takeScreenshot("Proceeding to checkout")
        self.click(self.CHECKOUT_BUTTON)
