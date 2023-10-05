# Nesse programa podemos colocar em questão que há um requisito mínimo para o aluno atingir, que seria de 85

gpa = float(input('What was your Grade Point avarage? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85:
    if lowest_grade >= .70:
        print('Well done!!!')

# O que está sendo dito aqui é que há dois requisitos aqui, ambos requisitos devem ser atendidos para que o aluno entre para o quadro de honra, sendo colocado na linha de código o "and".

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True

else:
    honour_roll = False

    if honour_roll:
        print('Well Done!!!')

# Como aqui mostra o formado da linha com o "and", é bem mais simples de ser lido e evita de você colocar um erro de recuo. Também a forma como o "and" são processadas é que AMBAS AS CONDIÇÕES DEVEM SER VERDADEIRAS, para que a condição seja avaliada como verdadeira, então vamos voltar a isso, se tivermos um GPA que não fosse superior a 85, digamos que o seu GPS fosse 70%, então você não vai para o quadro de honra e isso serve para as notas que sejam abaixo disso, pois ambas as condições precisam ser atendidas para que seja aceita a sua nota no quadro de honra e apareça a frase "Well done!".