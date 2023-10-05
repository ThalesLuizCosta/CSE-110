tip = float(input("What is the tip amount? $"))

while tip < 0:
    print("Sorry, the tip cannot be nagative")
    tip = float(input("What is the tip amount? $"))

print(f"You have tipped an amount of ${tip:.2f}")

# quando se coloca o "while" o código irá somente colocar o que está dentro desse valor de "tip", então ele retornará para a linha 3, neste como em todos os casos nunca podemos esquecer de declarar a variável para assim chamar a função dessa variável.