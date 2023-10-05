quantity_from_user = input("How many items do you have? ")

# A variável "amount_from_user" é uma string.
# Para convertê-lo para um número inteiro você usa a notação int(...):
quantity_number = int(quantity_from_user)

# Como a variável quantidade_número é um número inteiro, você pode fazer contas com ela:
double_number = quantity_number * 2

# Se você quiser usar esses valores em strings, NÃO PODE simplesmente adicioná-los, primeiro
# tem que convertê-los em uma string:

# forma ERRADA: "print("Twice as many is: " + double_number)"

# forma CERTA:
double_string = str(double_number)
print("Twice as many is: " + double_string)

# Você também pode fazer isso em uma única etapa:
# forma CERTA:
print("Twice as many is " + str(double_number))

# Usando duas linhas:
people_string = input("How many people are in the room? ")
people_number = int(people_string)

# Usando uma linha:
people_number = int(input("How many people are in the room? "))

# O mesmo funciona para números de ponto flutuante:
length_number = float(input("What is the length? "))