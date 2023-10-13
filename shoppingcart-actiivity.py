shopping_cart = []

while True:
    # Exibe o menu de opções
    print("\nMenu:")
    print("1. Add to shopping cart")
    print("2. See itens added")
    print("3. Exit")
    
    choose = input("Choose an option: ")
    
    if choose == "1":

        item = input("Enter the name of the item you want to add to the cart: ")
        shopping_cart.append(item)
        print(f"{item} has been added to cart.")
    elif choose == "2":

        if shopping_cart:
            print("\nItems in cart:")
            for i in range(len(shopping_cart)):
                    item = shopping_cart[i]
                    print(f"{i}- {item}")
        else:
            print("The cart is empty.")

    elif choose == "3":

        print("Thank you for using the shopping cart. Check back often!")
        break
    
    else:

        print("Invalid option. Please choose a valid option.")
