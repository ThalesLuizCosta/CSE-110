province = input('What province do you live in? ')
tax = 0.0

if province == 'Alberta' or province == 'Nunavut' or province == 'Yukon' or province == 'Manitoba' or province == 'Saskatchewan':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
print(tax)

    # Aqui acima eu usei a forma de escrever o código usando o "or" para colocar mais de um local para calcular a taxa de imposto que será a mesma para os dois locais ou mais.

    # IMPORTE DICA: SEMPRE TESTE AS FORMAS PARA VER SE ESTÁ DA FORMA CORRETA E ASSIM GARANTINDO QUE ESTEJA TENDO O RESULTADO ESPERADO!