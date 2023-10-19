shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = -1
max_product = "" # Não importa o que você defina isso, ele só precisa ser declarado no "output"

for item in shopping_cart:
    product_name = item[0] # O nome do produto é a primeira parte
    price = item[1] 

    if price > max_price:
        # esse é o produto com o maior preço
        max_price = price

        # é importante salvar também o nome deste produto como o produto mais caro
        max_product = product_name

print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")