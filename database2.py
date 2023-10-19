colors = "red green blue yellow"

colors_parts = colors.split() # o algoritmo split serve para separar a string em substring, tenho em vista que o "()" vazio não delimita o número máximo de separações e nem o que será separado, por exemplo "date_parts = colors.split(/)" irá separar uma data assim ['15', '08', '1984'], você também pode usar o "split" com um número máximo de divisões usando o "colors_parts = colors.split(maxsplit=2) e "lembre-se que a contagem sempre começa pelo "0" e não pelo número "1"." 

print(colors)
print(colors_parts)

for colors in colors_parts: # com essa função você faz o output no formato que ele lerá cada cor em uma linha
    print(colors)

second = colors_parts[1] # essa parte já é para mostrar que a palavra a ser repetida será somente a qual é inserida no "[]", neste caso o "1", então somente a cor será enumerada constará no "output", no caso o green.

print(second)