pi = 3.14159
print (pi)
# é uma função normal de impressão de números como sem chamar o ' '.
first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num - second_num)
print(first_num * second_num)
print(first_num ** second_num)
print(first_num / second_num)
print(first_num // second_num)
print(first_num % second_num)
# são operações matemáticas simples
# days_in_feb = 28 -> print(days_in_feb + 'days in February'), o python não entenderá qual tipo de função ele deve colocar, se é uma frase ou se é uma operação matemática
days_in_feb = 28
print(str(days_in_feb) + ' days in February')
# esta é a forma correta, colocando o 'str na frente e "(com a string aqui dentro)" para assim ela não possa ser tratada como somente uma string sem valor agredado.

# Assim como as operações matemáticas diferentes, pois aqui você pode forçar a ser feito de outro jeito, tendo a adição feita antes da multiplicação(como normalmente é feito na matemática convencional).
count = (3 + 4) * 2
print(count) 