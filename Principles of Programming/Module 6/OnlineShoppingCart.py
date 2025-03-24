class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print("{} {} @ ${} = ${}"
              .format(self.item_name, self.item_quantity, self.item_price, self.item_cost()))

    def item_cost(self):
        return round(self.item_price * self.item_quantity, 2)

    def print_item_description(self):
        print("{}: {}"
              .format(self.item_name, self.item_description))


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
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item: ItemToPurchase):
        if modified_item.item_name != "none":
            for item in self.cart_items:
                if item.item_name == modified_item.item_name:
                    if modified_item.item_price != 0.0:
                        item.item_price = modified_item.item_price
                    if modified_item.item_quantity != 0:
                        item.item_quantity = modified_item.item_quantity
                    return
            print("Item not found in cart. Nothing modified.")

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
        print(self.customer_name, "'s", "Shopping Cart -", self.current_date)

        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
            return
        
        print("Number of Items:", self.get_num_items_in_cart())
        total = 0
        for item in self.cart_items:
            item.print_item_cost()
            total+= item.item_cost()
        print("\nTotal: ${}".format(total))


    def print_descriptions(self):
        print(self.customer_name, "'s", "Shopping Cart -", self.current_date)
        print("Item Descriptions")
        [item.print_item_description() for item in self.cart_items]
        
def print_menu():
    menu_string = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "Choose an option:\n"
    )
    print(menu_string)
    
NUMBER_OF_ITEMS_TO_FETCH = 2
items_list = []
item_count = 0
for count in range(NUMBER_OF_ITEMS_TO_FETCH):
    item = ItemToPurchase()

    while True:
        item_name = input('Enter the item name:\n')
        if not item_name.strip():
            print("Cannot have blank or empty Item Name. Please try again!")
        else:
            item.item_name = item_name
            break

    while True:
        try:
            item.item_price = float(input('Enter the item price:\n'))
            break
        except Exception as err:
            print("Invalid Item Price. Please try again!")
            
    while True:
        try:
            item.item_quantity = int(input('Enter the item quantity:\n'))
            break
        except Exception as err:
            print("Invalid Item Quantity. Please try again!")

    items_list.append(item)

print("\nTOTAL COST\n")
total = 0
for item in items_list:
    item.print_item_cost()
    total+= item.item_cost()

print("\nTotal: ${}".format(total))

my_shopping_cart = ShoppingCart("test", "")

my_shopping_cart.add_item(items_list[0])
print(my_shopping_cart.cart_items[0].item_name)
#my_shopping_cart.remove_item(items_list[0].item_name)

print(my_shopping_cart.cart_items[0].item_name)
my_shopping_cart.total()
my_shopping_cart.print_descriptions()

while True:
    print_menu()
    menu_selected = input()
    match menu_selected.lower():
        case 'a':
            print(menu_selected)
        case 'r':
            print(menu_selected)
        case 'c':
            print(menu_selected)
        case 'i':
            print(menu_selected)
        case 'o':
            print(menu_selected)
        case 'q':
            break
            
