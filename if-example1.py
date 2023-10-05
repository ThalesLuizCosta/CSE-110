price = input('How much did you pay? ')

price = float(price) # Sub variável
if price >= 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))

# Neste caso acima temos uma variável imposta no final  da primeira linha de código e depois na linha seguinte segue-se querendo saber como uma "sub variável" declarada em "float", o que traz ela para a questão do "então se" na terceira linha, o que conduz a operação em relação a taxa de imposto que será passada ao final de tudo como uma "string" e não como um "numeral" de fato. 

else:
    tax = 0
    print(tax)
    print('Tax rate is: ' + str(tax)) # Esta operação resulta na frase com o número(já transformado em string) em casas decimais.

price = input('How much did you pay? ')
price = float(price)

if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Tax rate is: ' + str(tax)) # Neste caso há como somente colocar a frase final para trazer o resultado esperado da operação.

# > maior que
# < menor que
# >= maior ou igual que
# <= menor ou igual que
# == igual a
# != não é igual a