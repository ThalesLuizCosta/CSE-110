child_food = float(input("What is the price of a child's meal? "))
child_drink = float(input("What is the price of a child's drink? "))
adult_food = float(input("What is the price of a adult's meal? "))
adult_drink = float(input("What is the price of a adult's drink? "))
child_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))

subtotal_food = (child_food * child_number) + (adult_food * adult_number)
subtotal_drink = (child_drink * child_number) + (adult_drink * adult_number)
subtotal = float(subtotal_food + subtotal_drink)

print("O subtotal é = $", subtotal)

subtotal = (subtotal)

tax_rate = float(input("What is the sales tax rate? "))
sales_tax = float(subtotal * tax_rate / 100)

print("Sales Tax: $",sales_tax)

total = float(subtotal + sales_tax)

print("$", total)

payment_amount = float(input("What is the paymount amount? "))

print(f"Change: $", (payment_amount) - (total))

change = payment_amount - total

print(f"Change: $ {change:.3}")