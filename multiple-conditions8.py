country = input('What country do you live in? ')
province = input('What province do you live in? ')
tax = 0.0
if country == ('Canada'):
        province = input('What province do you live in? ')
        if province in('Alberta', \
                   'Nunavut', 'Yukon', 'Manitoba', 'Saskatchewan'):
            tax = 0.05
        elif province == 'Ontario':
            tax = 0.13
elif country == ('Brasil'):
        if province in('São Paulo', \
                      'Parana', 'Santa Catarina', 'Rio Grande do Sul'):
              tax = 5.25
else:
    tax = 2.75
print(tax)
    
    # Para esse caso acima foi colocado mais de um "if", "elif" e "else" para que seja informado qual é a taxa de imposto para quem não é canadense.

    # IMPORTE DICA: SEMPRE TESTE AS FORMAS PARA VER SE ESTÁ DA FORMA CORRETA E ASSIM GARANTINDO QUE ESTEJA TENDO O RESULTADO ESPERADO!