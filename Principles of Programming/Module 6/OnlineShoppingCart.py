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
        print("\nTotal: ${}".format(round(total, 2)))


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
        "Choose an option:"
    )
    print(menu_string)


shopping_cart = ShoppingCart()


def check_if_shopping_cart_present():
    if shopping_cart.customer_name == "none":
            print("Create Shopping Cart First")
            create_shopping_cart()

def create_shopping_cart():
    while True:
        customer_name = input('Enter Customer Name:\n')
        if not customer_name.strip():
            print("Cannot have blank or empty Customer Name. Please try again!")
        elif customer_name.strip() == "none":
            print("Cannot have none as Customer Name. Please try again!")
        else:
            shopping_cart.customer_name = customer_name
            break

    while True:
        current_date = input('Enter Current Date:\n')
        if not current_date.strip():
            print("Cannot have blank or empty Current Date. Please try again!")
        else:
            shopping_cart.current_date = current_date
            break

def add_item_to_cart():
    if shopping_cart.customer_name == "none":
        print("Create shopping Cart First")
        create_shopping_cart()
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

    while True:
        try:
            item.item_description = input('Enter the item description:\n')
            break
        except Exception as err:
            print("Invalid Item Descruotion. Please try again!")        

    shopping_cart.add_item(item)

def remove_item_from_cart():
    item_to_be_removed = input('Enter the item name to be removed:\n')
    shopping_cart.remove_item(item_to_be_removed.strip())
    
def modify_item_quantity():
    item_name_to_be_modified = input('Enter the item name to be modified:\n')
    while True:
        try:
            new_item_quantity = int(input('Enter the new item quantity:\n'))
            break
        except Exception as err:
            print("Invalid Item Quantity. Please try again!")
    shopping_cart.modify_item(ItemToPurchase(item_name=item_name_to_be_modified, item_quantity=new_item_quantity))     
    
def output_shopping_cart():
    print("\nOUTPUT SHOPPING CART")
    shopping_cart.total()

def output_items_description():
    print("OUTPUT ITEMS' DESCRIPTIONS")
    shopping_cart.print_descriptions()

while True:
    print_menu()
    menu_selected = input()
    match menu_selected.lower():
        case 'a':
            add_item_to_cart()
        case 'r':
            remove_item_from_cart()
        case 'c':
            modify_item_quantity()
        case 'i':
            output_items_description()
        case 'o':
            output_shopping_cart()
        case 'q':
            break
            
