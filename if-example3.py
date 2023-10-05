country = input('Enter the name of your home country: ')
if country == 'brasil':
    print('So you must like surf!')
else:
    print('You are not from Brasil')

    # Nesta caso é feita uma comparação com as strings para mostrar o que acontece em cada um dos resultados, o resultado só será "So you must like hockey" se você colocar todas as letras exatamente igual a string pedida para o "if". Mas isso pode ser corrigido se caso vc coloque para que a variável seja informada da mesma forma que o resultado esperado(a menos que os caractéres sejam diferentes, daí o resultado será negativo ao pedido).

    country = input('Enter the name of your home country: ')
if country.lower() == 'brasil':
    print('So you must like surf!')
else:
    print('You are not from Brasil')