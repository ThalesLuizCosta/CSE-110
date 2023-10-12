friends = ["Daniel", "Lucas", "Davi", "Tamer"]
tips = [13.35, 10.50, 12.75, 15.15] 

# lembrando que nesse caso não se pode misturar os dados, se for nome então que seja somente nome, se for números, então que só seja números.
running_total = 0

for tip_amount in tips:
    running_total = running_total + tip_amount
    # uma outra forma de fazer esse linha é "running_total += tip_amount".

print(f"The total is: {running_total:.2f}")

# Tecnicamente, você pode misturar tipos de variáveis e ter uma lista que contém diferentes tipos de variáveis (por exemplo, cadeias de caracteres e números), mas muitas vezes torna mais difícil trabalhar com a lista mais tarde, então isso geralmente é desencorajado. Em vez disso, faça uma lista que tenha um propósito claro e coloque apenas as coisas que pertencem. Então, se necessário, faça outra lista para outras coisas.