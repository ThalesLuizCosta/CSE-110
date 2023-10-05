first_name = 'Thales Luiz'
last_name = 'Costa'
#space = ' '
#print(first_name + space + last_name)
#print('Hello, ' + first_name + space + last_name)
#first_name = input('Please enter your first name: ')
#last_name = input('Please enter your last name: ')
#print('Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize())
#Quando se tem o parênteses depois da função, significa que está anulando aquela forma de entrada da variável, deixando assim como se específica na função.
#output = 'Hello, ' + first_name + ' ' + last_name
#output = 'Hello, {1}, {0}'.format(first_name, last_name)
#print(output)
#De acordo com as numereções que estiverem dentro das chaves, dirá como será escrito dentro da chamada pelo "output".
output1 = f'Hello, {first_name} {last_name}'
output2 = 'Hello, {1}, {0} {1}'.format(first_name, last_name)
output3 = 'Hello, ' + first_name + ' ' + last_name
output4 = 'Hello, ' + last_name + ', ' + first_name
print(output1)
print(output2)
print(output3)
print(output4)
#Como mostrado nestes vídeos, algumas funções de string úteis disponíveis em Python são: words = "the cat IN THE hat" = the cat IN THE hat, words.capitalize() = The cat in the hat, words.title() = The Cat In The Hat, words.upper() = THE CAT IN THE HAT, words.lower() = the cat in the hat, words.count("t") = 3, words.lower().count("t") = 4