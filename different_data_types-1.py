color = 'blue'
animal = 'horse'

# Você pode adicionar, ou concatenar, duas strings juntas com +:
print(color + animal)
# This displays: bluehorse

# Você pode adicionar várias strings juntas, no entanto as strings são variáveis ou diretamente nas aspas:
print(color + ' ' + animal + '!')
# This displays: blue horse!

# Você também poderá salvador o resultado em uma nova string variável:
combined_words = color + ' ' + animal + '!'
print(combined_words)
# Por outro lado, se o tipo de dados das variáveis for inteiro ou ponto flutuante, o operador realmente realiza a adição matemática:+
boys_count = 10
girls_count = 12

# Adicione dois números juntos usando o operador +:
print(boys_count + girls_count)

# Você pode salvar o resultado em uma nova variável para usar letras no lugar:
total_count = boys_count + girls_count
print(total_count)

apple_count = 5

# "print('You have ' + apple_count + ' apples')" essa forma de fazer está ERRADA!!!

print('You have ' + str(apple_count) + ' apples') # essa forma de fazer está CERTA!!!