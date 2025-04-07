from shopping_cart import ShoppingCart
from item_to_purchase import ItemToPurchase
from utils import *

def print_menu():
    print()
    menu_string = [
        "MENU",
        "a - Add item to cart",
        "r - Remove item from cart",
        "c - Change item quantity",
        "i - Output items' descriptions",
        "o - Output shopping cart",
        "q - Quit"
    ]
    for menu_item in menu_string:
        aligned_print(menu_item)
    
def create_shopping_cart() -> ShoppingCart:
    shopping_cart = ShoppingCart()
    while True:
        customer_name = aligned_input("Enter customer's name:\n")
        if not customer_name.strip():
            aligned_print("Cannot have blank or empty Customer Name. Please try again!")
        elif customer_name.strip() == "none":
            aligned_print("Cannot have none as Customer Name. Please try again!")
        else:
            shopping_cart.customer_name = customer_name
            break

    while True:
        current_date = aligned_input("Enter today's date\n")
        if not current_date.strip():
            aligned_print("Cannot have blank or empty Current Date. Please try again!")
        else:
            shopping_cart.current_date = current_date
            break
    print()
    aligned_print(f"Customer name: {customer_name}")
    aligned_print(f"Today's date: {current_date}")
    
    return shopping_cart
        

def add_item_to_cart(shopping_cart: ShoppingCart):
    item = ItemToPurchase()
    while True:
        item_name = aligned_input('Enter the item name:\n')
        if not item_name.strip():
            aligned_print("Cannot have blank or empty Item Name. Please try again!")
        else:
            item.item_name = item_name
            break

    while True:
        try:
            item.item_description = aligned_input('Enter the item description:\n')
            break
        except Exception as err:
            aligned_print("Invalid Item Descruotion. Please try again!")
            
    while True:
        try:
            item_price = float(aligned_input('Enter the item price:\n'))
            if item_price <= 0:
                aligned_print("Item Price Cannot be negative or zero")
                continue
            else:
                item.item_price = item_price
                break
        except Exception as err:
            aligned_print("Invalid Item Price. Please try again!")
            
    while True:
        try:
            item_quantity = int(aligned_input('Enter the item quantity:\n'))
            if item_quantity <= 0:
                aligned_print("Item Quantity Cannot be negative or zero")
                continue
            else:
                item.item_quantity = item_quantity
                break
        except Exception as err:
            aligned_print("Invalid Item Quantity. Please try again!")          

    shopping_cart.add_item(item)

def remove_item_from_cart(shopping_cart: ShoppingCart):
    if shopping_cart.get_num_items_in_cart() == 0:
        aligned_print("Shopping cart is empty! Nothing to remove")
    else:
        item_to_be_removed = aligned_input('Enter the item name to be removed:\n')
        shopping_cart.remove_item(item_to_be_removed.strip())
    
def modify_item_quantity(shopping_cart: ShoppingCart):
    if shopping_cart.get_num_items_in_cart() == 0:
        aligned_print("Shopping cart is empty! Nothing to modify")
        return
    item_name_to_be_modified = aligned_input('Enter the item name to be modified:\n')
    while True:
        try:
            new_item_quantity = int(aligned_input('Enter the new item quantity:\n'))
            if new_item_quantity <= 0:
                aligned_print("Item Quantity Cannot be negative or zero")
                continue
            else:
                break
        except Exception as err:
            aligned_print("Invalid Item Quantity. Please try again!")
    shopping_cart.modify_item(ItemToPurchase(item_name=item_name_to_be_modified, item_quantity=new_item_quantity))     
    
def output_shopping_cart(shopping_cart: ShoppingCart):
    aligned_print("SHOPPING CART")
    shopping_cart.total()

def output_items_description(shopping_cart: ShoppingCart):
    aligned_print("ITEMS' DESCRIPTIONS")
    shopping_cart.print_descriptions()
