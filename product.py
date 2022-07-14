class Product:
    # name, price, colour
    def __init__(self, name, price, storage, colour):
        self.name = name
        self.price = price
        self.storage = storage
        self.colour = colour

    def print_product(self):
        print(f"{self.name} ${self.price}")


iPhone12 = Product("iPhone 12", 1199)
print(iPhone12.print_product())