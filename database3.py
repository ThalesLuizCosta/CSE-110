name = "\tBrother Costa  \n" # nesse caso o "\t" faz com que haja espaço no início da string e o "\n" para fazer um novo parágrafo.
 
clean_name = name.strip() # o "strip" no caso leva a função de retirar algo do que se é pedido para mostrar, como no caso os espaços antes e depois do meu nome, que são indicados pelo espaço vazio entre os parênteses e quando for colocado algo em específico, então aquela função será específica.

# ou se quiser usar a mesma função de forma mais simples basta colocar o "name = name.strip()" sem que haja a necessidade de inventar mais uma função, levando a mostrar pela função: 

# "print(f"---{clean_name}---")".

print(f"---{name}---")