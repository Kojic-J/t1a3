from os import system
from item_list import Products, print_products
from product import Product

iPhone12 = Product("iPhone 12", 1199)
iPhone12big = Product("iPhone 12", 1199)

products = Products((iPhone12, iPhone12big))
Products.print_products()

# display options +
# ask for and return input from user
# display colours, products
# add devices
# remove devices
# run program (fav colour, devices owned, devices wanted, storage needs, main use)


def options_page():
    print("a. Show products")
    print("b. Show colours")
    print("c. Add devices")
    print("d. Remove devices")
    print("e. Begin")
    print("f. Leave")
    selection = input("Choose an option: a-f ")
    return selection


def add_device():
    name = input("What is the device called? ")
    price = float(input("What is the price?"))
    colour = input("What colour is it? ")
    storage = input("How much storage does it have? ")


def begin():
    print("What's your favourite colour from displayed options? ")


menu = ""

while menu != "f":
    system('clear')
    menu = print_products()
    system('clear')
if menu == "a":
    print_products()
if menu == "b":
    display_colours()
if menu == "c":
    add_device()
if menu == "d":
    remove_device()
if menu == "e":
    begin_program()
elif menu == "f":
    continue
else:
    print("Try selecting from the list")
