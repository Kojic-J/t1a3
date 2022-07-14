# list of apple products
from product import Product


class Products:
    def __init__(self, products):
        self.products = products


def print_products(self):
    print("These are the Apple products we can recommend! Feel free to add more!")
    for item in self.products:
        item.print_product()


iPhone12 = Product("iPhone 12", 1199)
iPhone12big = Product("iPhone 12", 1199)

products = Products((iPhone12, iPhone12big))
Products.print_products()
