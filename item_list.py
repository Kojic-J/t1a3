# list of apple products
from products import Device


class device_list:
    def __init__(self, products):
        self.products = products

    def print_products(self):
        print("These are the Apple products we can recommend! Feel free to add more!")
        for item in self.products:
            item.print_product()

    def add_device(self, name, price, storage, colour):
        new_device = Device(name, price, storage, colour)
        self.products.append(new_device)
