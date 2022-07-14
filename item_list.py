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

    def delete_device(self, name):
        for item in self.products:
            if item.name == name:
                self.products.remove(item)
                return print(f"{name} removed successfully")
        return print(f"{name} does not exist on the list yet! Try adding the device.")

# add boolean do you like your new device?
