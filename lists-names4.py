clients = []

new_client = ""
while new_client != "quit":
    new_client = input("What is the name of a client? ")
    clients.append(new_client)

for client in clients:
    print(f"Welcome to my store",(client))

# Neste caso usando o "while", a lista será preenchida até o campo "client" ser preenchido com a palavra "it's over!", mostrando assim todos os clientes listados quando perguntado quem eles são, isso é possível de ser feito graças ao "while" e também o encerramento é devido ao "!=", mostrando que só será dado por encerrado quando for escrito "it's over!", lembrando que quando se é colocado lá em "clients" o "[]", o código só rodará com ele, não com "()" e nem com "{}".