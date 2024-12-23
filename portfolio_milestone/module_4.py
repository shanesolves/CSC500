class ItemToPurchase:
    def __init__(self):
        # attributes we need to initialize
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        # cost details for item
        total_cost = self.item_price * self.item_quantity
        print(self.item_name + " " + str(self.item_quantity) + " @ $" + str(round(self.item_price, 2)) + " = $" + str(round(total_cost, 2)))

def main():
    # create first item
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    # create second item
    print("\nItem 2")
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    # print item costs
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    # calculate and print total cost
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print("\nTotal: $" + str(round(total_cost, 2)))


if __name__ == "__main__":
    main()