degrees_f = float(input("What is the temperature in Fahrenheit? "))
degrees_c = (degrees_f - 32) * 5 / 9

print(f"The temperature in Celsius is {degrees_c:.1f} degrees.")

# Nota: Eu escolhi "degrees_f" em vez de "degrees_fahrenheit", pq eu decidi que "_f" e "_c" são comuns, como abreviações conhecidas e ao menos como introducão de bugs mais do que se eu tentasse intruduzir "fahrenheit" no meu código a cada vez. Mas até nesse caso, eu achei que "degrees_f" se parece mais óbvio que uma simples letra variável de "f".