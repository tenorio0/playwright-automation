from core.pages.base_page import BasePage


class HomePage(BasePage):
    PRODUCTS_TITLE = '[data-test="title"]'
    CART_BADGE = '[data-test="shopping-cart-badge"]'
    CART_LINK = '[data-test="shopping-cart-link"]'
    INVENTORY_LIST = '[data-test="inventory-list"]'

    def should_be_on_inventory_page(self) -> None:
        self.assert_contains_text(self.PRODUCTS_TITLE, "Products")
        self.assert_url_contains("/inventory.html")
        self.takeScreenshot("Inventory page displayed")

    def should_list_products(self) -> None:
        self.assert_visible(self.INVENTORY_LIST)
        self.takeScreenshot("Product catalog displayed")

    def add_product_to_cart(self, product_slug: str) -> None:
        add_to_cart_button = f'[data-test="add-to-cart-{product_slug}"]'
        self.scroll_to_element(add_to_cart_button)
        self.takeScreenshot(f"Adding product to cart -> {product_slug}")
        self.click(add_to_cart_button)

    def should_have_cart_badge(self, quantity: int) -> None:
        self.assert_text(self.CART_BADGE, str(quantity))
        self.takeScreenshot(f"Cart badge updated to {quantity}")

    def open_cart(self) -> None:
        self.takeScreenshot("Opening cart")
        self.click(self.CART_LINK)
