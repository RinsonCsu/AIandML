class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0  

    def print_item_cost(self):
        print("{} {} @ ${} = ${}"
              .format(self.item_name, self.item_quantity, self.item_price, self.item_cost()))

    def item_cost(self):
        return round(self.item_price * self.item_quantity, 2)

NUMBER_OF_ITEMS_TO_FETCH = 2
items_list = []
item_count = 0
while item_count < NUMBER_OF_ITEMS_TO_FETCH:
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
    item_count += 1

print("\nTOTAL COST\n")
total = 0
for item in items_list:
    item.print_item_cost()
    total+= item.item_cost()

print("\nTotal: ${}".format(total))

            
