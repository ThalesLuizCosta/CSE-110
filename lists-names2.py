clients = []

clients.append("Thales")
clients.append("Pamela")
clients.append("Eva")

for client in clients:
    print(client)

# Neste caso a forma pela qual será mostrada a lista de clientes pode ser feita de diversas formas, como por exempo usando o termo ".append" após o que mostrará no terminal sem os "[]" antes e depois dos nomes, mas ao ser usado o "for client in clients:" a lista de clientes apareceu sem estar com os "[]" antes e depois dos nomes, pois está sendo buscado o "client" e não "clients", o que geraria uma lista repetida com os nomes entre os cochetes.