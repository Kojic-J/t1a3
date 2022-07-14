from os import system
from item_list import device_list
from products import Device
from seed import seed

list = seed()

# display options +
# ask for and return input from user
# display colours, products
# add devices
# remove devices
# run program (fav colour, devices owned, devices wanted, storage needs, main use)

# display user options


def options_page():
    print("a. Show products")
    print("b. Show colours")
    print("c. Add devices")
    print("d. Remove devices")
    print("e. Begin")
    print("f. Leave")
    selection = input("Choose an option: a-f ")
    return selection

# function for adding a device


def add_device():
    name = input("What is the device called? ")
    price = float(input("What is the price of {name}? "))
    colour = input("What colour is the {name}? ")
    storage = input("How much storage does {name} have? ")
    device_list.add_device(name, price, colour, storage)

# function to begin program


def begin():
    print("What's your favourite colour from displayed options? ")


# confirm string response
selection = ""
# while, if/else loop to decide what to do when option selected
# display item names, storage and colours available
while selection != "f":
    system('clear')
    selection = print_products()
    system('clear')
if selection == "a":
    print_products()
if selection == "b":
    display_colours()
if selection == "c":
    add_device()
if selection == "d":
    remove_device()
if selection == "e":
    begin_program()
elif selection == "f":
    continue
else:
    print("Try selecting from the list")

    input("Press Enter to continue ")
    system('clear')

print("Thanks!")
