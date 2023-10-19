# Lê os dados do arquivo
with open('dados.txt', 'r') as archieve:
    linhas = archieve.readlines()

# Converte as linhas para números inteiros
ages = [int(linha.strip()) for linha in linhas]

# Calcula a média das idades
average_age = sum(ages) / len(ages)

print(f"Média das idades: {average_age:.2f}")

# Verifica quais idades estão acima ou abaixo da média
above_average = [age for age in ages if age > average_age]
below_average = [age for age in ages if age < average_age]

print(f"Idades acima da média: {above_average}")
print(f"Idades abaixo da média: {below_average}")