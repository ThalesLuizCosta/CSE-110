people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Comece nossa variável "youngest_age" em algo maior do que qualquer um que encontraremos
youngest_age = 9999

# mostrará o nome da pessoa mais jovem
youngest_name = ""

# percorra cada pessoa na lista
for person_line in people:

    parts = person_line.split() # por padrão, isso irá dividir os espaços

    # define variáveis para as duas partes diferentes
    name = parts[0]
    age = int(parts[1])

    # verifique se essa pessoa atual é mais jovem do que a mais nova listada que vimos até agora

    if age < youngest_age:
        # esta pessoa é a "mais nova"

        # salve a idade como a pessoa mais nova
        youngest_age = age

        # salve o nome como a pessoa mais nova
        youngest_name = name

# após terminar o loop, será mostrado o resultado pedido na lista
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")
