names = ["Daniel", "Lucas", "Davi", "Tamer"]
numbers = ["33574050", "33952716", "33101984", "33614748"]

# ...
# Code here that populates the two lists
# ...

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f"{name} - {number}")

    # às vezes você tenha uma situação onde você terá 2 listas que você quer trabalhar paralelamente. Por exemplo, na primeira lista terá o nome dos seus amigos, e na segunda lista o número de telefone deles. Se você quiser iterar essas duas listas e mostra-las na tela, você não poderá usar o loop "for name in names:", pq você não teria nada correspondente aos números de telefone deles nesse loop.
    
    # A solução mais comum para este problema é percorrer os índices que correspondem a uma das listas e então você pode acessar o item de cada lista nesse índice, como está acima.

    # Lembre-se de que em casos como esse você deve ter muito cuidado para que as duas listas não fiquem fora de sincronia. Em cursos futuros, você aprenderá outras técnicas para combinar dois elementos em um único tipo de dados, para que possa mantê-los sempre juntos.