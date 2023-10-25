import datetime

# imprime marcas de data/hora para ver quanto tempo as seções de código levam para serem executadas.

def print_time():       # o algoritmo "def" é usado para definir funções
    print('task completed')    # sempre tomar cuidado com a identação para que seja executado o código de forma correta, pois a identação determina quais linhas de código pertencem a esta função.
    print(datetime.datetime.now())
    print()

first_name = 'Thales'
print_time()

for x in range(0,10):
    print(x)
print_time()    # essa é uma maneira mais limpa de chamar a função "now()"

# esse exemplo mostra o tempo que demorou para ser impresso o resultado do código no display, assim como foi mostrado no arquivo "functions1.py". Quando se escreve dessa forma, para o computador se torna menos prolixo para chamar uma função dentro de uma biblioteca com o mesmo nome da função.