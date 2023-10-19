# courses_file = open("dataexample.txt") -> essa linha serve para abrir arquivos que estão em outros locais, mas sempre presica ser especificado o caminho para esse arquivo ou o nome dele.

with open("dataexample.txt") as courses_file: # essa é uma outra forma para abrir o arquivo desejado 
    for line in courses_file:
        
        parts = line.split(",")

        name = parts[0]

        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f"{name} - Grade: {grade}, after bonus {bonus_grade}")

# courses_file.close() -> nesse caso é sempre bom prestar atenção para dar um parâmetro para fechar o arquivo e liberar os recursos do sistema.

# a forma que foi feita acima mostra que é uma forma "elegante" de fechar o arquivo sem que haja desperdícios de recursos do sistema, tornando assim o o código mais seguro e limpo.