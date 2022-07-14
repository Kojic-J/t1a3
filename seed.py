from item_list import device_list
from products import Device


def seed():
    iPhone12 = Device("iPhone 12", 1199, "64GB", "Grey")
    iPhone12big = Device("iPhone 12", 1199, "64GB", "Grey")
    list = device_list((iPhone12, iPhone12big))
    return list
