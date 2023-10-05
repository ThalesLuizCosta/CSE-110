province = input('What province do you live in? ')
tax = 0.0

if province in('Alberta', 'Nunavut', 'Yukon', 'Manitoba', 'Saskatchewan'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
print(tax)

    # Já neste caso acima eu coloquei o "in" antes do parênteses para agrupar o conjunto de locais onde há a mesma alíquota de imposto, fazendo também com que o código fique um pouco menos cheio de marcações.

    # IMPORTE DICA: SEMPRE TESTE AS FORMAS PARA VER SE ESTÁ DA FORMA CORRETA E ASSIM GARANTINDO QUE ESTEJA TENDO O RESULTADO ESPERADO!