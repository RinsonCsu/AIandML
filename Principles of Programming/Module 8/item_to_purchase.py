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
