province = input('What province do you live in? ')
tax = 0.0

if province in('Alberta', \
                   'Nunavut', 'Yukon', 'Manitoba', 'Saskatchewan'):
    tax = 0.05
if province == 'Ontario':
    tax = 0.13
elif province == 'Quebec':
    tax = 0.15
else:
    tax = 0.0
print(tax)

    # Aqui acima eu colocarei como foi explicado anteriormente sobre o jeito de manter isso mais "limpo" e também "eficiênte", eu mudei o início do código para ficar mais "legível".

    # IMPORTE DICA: SEMPRE TESTE AS FORMAS PARA VER SE ESTÁ DA FORMA CORRETA E ASSIM GARANTINDO QUE ESTEJA TENDO O RESULTADO ESPERADO!