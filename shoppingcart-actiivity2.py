class shopping_cart:
    def __init__(self):
        self.itens = {}

    def add_item(self, item, price):
        if item in self.itens:
            self.itens[item] += price
        else:
            self.itens[item] = price

    def remove_item(self, item):
        if item in self.itens:
            del self.itens[item]
        else:
            print("Item not found in shopping cart.")

    def show_cart(self):
        total = 0
        print("Shopping Cart:")
        for item, price in self.itens.items():
            print(f"{item}: R${price:.2f}")
            total += price
        print(f"Total: R${total:.2f}")
        return total


cart = shopping_cart()

while True:
    print("\nMenu:")
    print("1 - Add item to cart")
    print("2 - Show Cart")
    print("3 - Remove item from cart")
    print("5 - Exit")
    print()
    choose = input("Choose the option: ")

    if choose == "1":
        print()
        item = input("Type item name: ")
        print()
        price = float(input("Type item price:R$ "))
        print()
        cart.add_item(item, price)
        print(f"{item} added to cart, Wohooo!")

    elif choose == "2":
        print()
        cart.show_cart()

    elif choose == "3":
        print()
        item = input("Type the name of the item you want to remove: ")
        cart.remove_item(item)
        print(f"{item} Removed from cart.")

    elif choose == "4":
        print()
        print("Thank you for using our shopping cart, I hope you found everything you wanted, have a great day and come back often!")
        print()
        break

    else:
        print("Invalid option, try again. :(")
