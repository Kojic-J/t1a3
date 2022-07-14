class Device:
    def __init__(self, name, price, storage, colour):
        self.name = name
        self.price = price
        self.storage = storage
        self.colour = colour

    def print_product(self):
        print(f"{self.name}: ${self.price}: {self.storage}: {self.colour}")


iPhone12 = Device("iPhone 12", 1199, "64GB", "Grey")
iPhone12.print_product()
