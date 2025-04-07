from utils import *
from item_to_purchase import ItemToPurchase

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        
    def add_item(self, item_to_purchase: ItemToPurchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                aligned_print("Item Removed!")
                return
        aligned_print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item: ItemToPurchase):
        if modified_item.item_name != "none":
            for item in self.cart_items:
                if item.item_name == modified_item.item_name:
                    if modified_item.item_quantity != 0:
                        item.item_quantity = modified_item.item_quantity
                        aligned_print("Item Quantity Modifed!")
                    return
            aligned_print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        cost = 0.0
        for item in self.cart_items:
            cost += item.item_price * item.item_quantity
        return cost

    def total(self):
        self.__print_heading()

        if self.get_num_items_in_cart() == 0:
            aligned_print("\nSHOPPING CART IS EMPTY")
            return
        aligned_print(f"Number of Items: {self.get_num_items_in_cart()}")
        total = 0
        for item in self.cart_items:
            item.print_item_cost()
            total+= item.item_cost()
        aligned_print("Total: ${}".format(round(total, 2)))


    def print_descriptions(self):
        self.__print_heading()
        
        if self.get_num_items_in_cart() == 0:
            aligned_print("\nSHOPPING CART IS EMPTY")
            return
        
        aligned_print("Item Descriptions")
        [item.print_item_description() for item in self.cart_items]

    def __print_heading(self):
        heading = f"{self.customer_name}'s Shopping Cart - {self.current_date}"
        aligned_print(heading)
