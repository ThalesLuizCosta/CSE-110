# lê o arquivo em específico
with open('datas.txt', 'r') as file:
    lines = file.readlines()

# converte as linhas em números inteiros
ages = [int(line.strip()) for line in lines]

# calcula a média de idade
average_age = sum(ages) / len(ages)

print(f"Average age: {average_age:.2f}")

# verifica as idades acima e abaixo da média
above_average = [age for age in ages if age > average_age]
below_average = [age for age in ages if age < average_age]

print(f"Ages above the average: {above_average}")
print(f"Ages below the average: {below_average}")