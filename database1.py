# courses_file = open("dataexample.txt") -> essa linha serve para abrir arquivos que estão em outros locais, mas sempre presica ser especificado o caminho para esse arquivo ou o nome dele.

with open("dataexample.txt") as courses_file: # essa é uma outra forma para abrir o arquivo desejado 
    for line in courses_file:
        print(line)

    print("Goodbye")

print("The file is closed now.")

# courses_file.close() -> nesse caso é sempre bom prestar atenção para dar um parâmetro para fechar o arquivo.