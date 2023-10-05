# BAD EXAMPLE: Este código usa a variável "nome" fora do loop para ser declarada

number = 0

while number < 10: 
    number = int(input("What is the number? "))
    name = input("What is your name?")

# print(f"Your name is: {name}")

# GOOD EXAMPLE: Este código primeiro declara a variável "nome" antes do loop, então pode ser usado posteriormente.

number = 0
name = ""

while number < 10: 
    number = int(input("What is the number? "))
    name = input("What is your name?")

print(f"Your name is: {name}")