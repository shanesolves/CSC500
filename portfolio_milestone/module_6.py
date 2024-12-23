class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def print_item_cost(self):
        return "{} {} @ ${} = ${}".format(self.name, self.quantity, self.price, self.price * self.quantity)

    def print_item_description(self):
        return "{}: {}".format(self.name, self.description)


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.description != "none":
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items: {}".format(self.get_num_items_in_cart()))
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(item.print_item_cost())
            print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        for item in self.cart_items:
            print(item.print_item_description())


def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option: ").lower()
        if choice == 'q':
            break
        elif choice == 'a':
            name = input("Enter the item name: ")
            description = input("Enter the item description: ")
            price = int(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(name, description, price, quantity))
        elif choice == 'r':
            name = input("Enter the name of the item to remove: ")
            cart.remove_item(name)
        elif choice == 'c':
            name = input("Enter the item name: ")
            description = input("Enter the new description (or 'none' to skip): ")
            price = int(input("Enter the new price (or 0 to skip): "))
            quantity = int(input("Enter the new quantity (or 0 to skip): "))
            cart.modify_item(ItemToPurchase(name, description, price, quantity))
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        else:
            print("Invalid choice. Please try again.")


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print("\nCustomer name: {}".format(customer_name))
    print("Today's date: {}\n".format(current_date))
    print_menu(cart)


if __name__ == "__main__":
    main()