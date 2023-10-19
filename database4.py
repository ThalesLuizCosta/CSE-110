numbers = [42, 25, 18, 83, 23, 85, 38, 2]

largest_so_far = numbers[0]

for number in numbers:
    if number > largest_so_far:
        # aqui mostra que esse número é maior do que o maior que vimos até agora.

        # e termina mostrando então que agora o maior que já vimos é...
        largest_so_far = number

# agora, depois do loop, vamos exibi-lo abaixo.
print(f"The largest is: {largest_so_far}")