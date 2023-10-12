# Primeiro prepare a lista.

print("Please enter the items of the shopping list (type: quit to finish):")

shopping_list = []
item = None # aqui está o "None", pois indica que não há itens em específico, mas que será inserido posteriormente.

while item != "quit":
    item = input("Item: ") # então aqui o "input" indica que o "item" será uma variável a ser inserida

    if item != "quit":
        shopping_list.append(item)

# Agora nós temos a lista, mostre no output:

print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

    # Eu poderia ter simplesmente colocado shopping_list[i] diretamente na minha declaração de impressão em vez de criar uma variável separada, se quisesse. Decidi fazê-lo desta forma para facilitar a leitura.

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

# esta linha acima mostra como mostrar os itens anteriores por causa do "[index]" e retirar o item selecionado pelo "index = int(input("Which item would you like to change? "))" para por um novo no lugar pelo "new_item = input("What is the new item? ")".

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

    # LEMBRANDO que o "\n" serve para criar um novo parágrafo.