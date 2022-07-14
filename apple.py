from os import system
from item_list import device_list
from products import Device
from seed import seed


list = seed()


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
    list.add_device(name, price, colour, storage)
    print(f"{name} has been added to the device list!")

# function to begin program


def print_products():
    pass


def display_colours():
    pass


def delete_product():
    # show the list of products, just names
    for item in list.products:
        print(item.name)
    # ask about the product we want to delete
    name = input("What is the product you want to delete? ")
    list.delete_item(name)


def begin_program():
    pass


def begin():
    print("What's your favourite colour from displayed options? ")


# confirm string response
selection = ""
# while, if/else loop to decide what to do when option selected
# display item names, storage and colours available
while selection != "f":
    system('clear')
    selection = options_page()
    system('clear')
    if selection == "a":
        list.print_products()
    if selection == "b":
        display_colours()
    if selection == "c":
        add_device()
    if selection == "d":
        delete_product()
    if selection == "e":
        begin_program()
    elif selection == "f":
        continue
    else:
        print("Select from the list")

    input("Press Enter to continue ")
    system('clear')

system('clear')
print("Thanks!")
