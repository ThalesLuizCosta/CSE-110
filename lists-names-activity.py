friends = []

name = None

    # Isso será usado no meu loop para pegar o nome de cada amigo que eu quero para colocar na lista. Posso iniciá-lo com qualquer valor, desde que esse valor não seja "end", caso contrário, nunca entrará no loop que fiz para reunir os nomes.

while name != "end":
    name = input("Type the name of a friend: ")
    if name != "end": # quando se coloca essa linha do "if" o "end" não irá ser mostrado no terminal.
        friends.append(name)

    print()
print("Your friends are:")

for friends in friends:
    print(friends)