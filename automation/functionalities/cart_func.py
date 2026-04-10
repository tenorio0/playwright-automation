from automation.pages.cart_page import CartPage
from automation.pages.home_page import HomePage


class CartFunc:
    def __init__(self, home_page: HomePage, cart_page: CartPage) -> None:
        self.home_page = home_page
        self.cart_page = cart_page

    def add_product_to_cart(self, product_slug: str) -> None:
        self.home_page.add_product_to_cart(product_slug)

    def open_cart(self) -> None:
        self.home_page.open_cart()

    def adicionar_produto_e_validar_carrinho(self, product_slug: str, product_name: str, quantity: int = 1) -> None:
        self.add_product_to_cart(product_slug)
        self.home_page.should_have_cart_badge(quantity)
        self.open_cart()
        self.cart_page.should_be_on_cart_page()
        self.cart_page.should_contain_product(product_name)
