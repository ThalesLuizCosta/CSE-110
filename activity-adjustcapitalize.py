first_name = 'Brigham'
last_name = 'Young'
space = ' '
print(first_name + space + last_name)
print('My name is, ' + space + first_name + space + last_name)
#Uma variável pode ser criada para conter uma função que poderá ser chamada em qualquer momento dentro da função específica a ser desempenhada#
sentence = 'My name is, Brigham Young'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('m'))
#Uma variável poderá ser também específicada para uma função única com o seu valor, como no exemplo acima#
first_name = input('What is your first name? ' ) 
last_name = input('What is your last name? ' )
print('My name is, ' + first_name + ' ' + last_name)
#Há algum motivo pelo qual as saídas das respostas não foram feitas de forma maiúscula, mas depois deu certo.#
print(space)
first_name = 'Brigham'
last_name = 'Young'

print(first_name + space + last_name)
output1 = f'Hello, {first_name} {last_name}'
output2 = 'Hello, {1}, {0} {1}'.format(first_name, last_name)
output3 = 'Hello, ' + first_name + ' ' + last_name
output4 = 'Hello, ' + last_name + ', ' + first_name
print(output1)
print(output2)
print(output3)
print(output4)