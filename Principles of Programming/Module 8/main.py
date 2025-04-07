from helper_functions import *
from utils import *
from shopping_cart import ShoppingCart
from item_to_purchase import ItemToPurchase

def main():
    shopping_cart = create_shopping_cart()
    while True:
        print_menu()
        menu_selected = aligned_input("Choose an option:\n")
        match menu_selected.lower():
            case 'a':
                add_item_to_cart(shopping_cart)
            case 'r':
                remove_item_from_cart(shopping_cart)
            case 'c':
                modify_item_quantity(shopping_cart)
            case 'i':
                output_items_description(shopping_cart)
            case 'o':
                output_shopping_cart(shopping_cart)
            case 'q':
                break
            case _:
                aligned_print_withline("Invalid menu option selected! Please try again")

main()
