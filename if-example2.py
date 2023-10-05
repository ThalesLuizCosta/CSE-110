country = 'CANADA'
if country == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')

# aqui nesse primeiro exemplo a resposta foi que o país não era o Canadá, pois estava em letras pequenas

country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')

# aqui nesse segundo exemplo a resposta foi que o país era o Canadá, pois foi colocado que os caractéres estavam em letras pequenas e que então seria aceito nesse caso, por conta do "country.lower() antes do ==".

country = input('Enter the name of your home country: ')
if country == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')