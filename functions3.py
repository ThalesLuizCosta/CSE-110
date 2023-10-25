from datetime import datetime

def print_time(task_name): # tente deixar um nome no "task_name" que faça sentido, para que não seja um problema para o programador futuro, deixe elas verem e tentarem advinhar para o que serve e comente, caso seja necessário.
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Thales'
print_time('first name assigned')
print(datetime.datetime.now())
print()

for x in range(0,10):
    print(x)
print_time('first name assigned')