# A maneira mais simples, foi recentemente adicionada ao python, e que é colocar um direito antes de sua string, como mostrado:f

car_count = 35
print(f"There are {car_count} cars on the road.")

# Outra abordagem é não usar o antes da cadeia de caracteres, mas em vez disso, usar depois da cadeia de caracteres, conforme mostrado:f.format()

print("There are {} cars on the road.".format(car_count))

# O efeito dessas abordagens é o mesmo, mas a primeira abordagem usando o "f" é um tipo de notação taquigráfica, para tornar as coisas mais simples e limpas. É importante saber sobre a segunda via, porque você vai vê-la usada em muitos exemplos de código na internet. Além disso, a segunda maneira é uma abordagem mais padrão que você verá em outras linguagens (por exemplo, Java, C#, etc.). Para este curso, você é bem-vindo a usar qualquer uma das abordagens, mas a maioria do material assumirá que você está usando a notação de cadeia de caracteres mais simples, de atalho "f".

# Em uma cadeia de caracteres de formato, você define a precisão ou o número de decimais a serem exibidos, colocando um após o nome da variável (alterando o 2 para o valor desejado).:.2f

# Os dois pontos (:) após o nome da variável indicam que você vai especificar como formatá-la.

# O ponto (.) indica que você está definindo a precisão ou o número de casas decimais.

# O número (2) indica que você gostaria que esse número de casas decimais fosse exibido

# O "f" indica que você deseja notação de ponto fixo.

# por exemplo:

cars = 3
people = 8

people_per_car = people / cars

# Arredondar para 1 casa decimal
print(f"There are {people_per_car:.1f} people in each car.")
# Saída: Há 2.7 pessoas em cada carro.

# Arredondar para 2 casas decimais
print(f"There are {people_per_car:.2f} people in each car.")
# Saída: Há 2.67 pessoas em cada carro.

# Arredondar para 3 casas decimais
print(f"There are {people_per_car:.3f} people in each car.")
# Saída: Há 2.667 pessoas em cada carro.

# Você pode dizer ao computador para exibir o número em notação científica, ou notação "expoente" usando após sua variável, onde define a precisão e indica que você está usando notação expoente.:.3e3e

distance = 9 * 1205 * 18

# Notação científica com 3 dígitos de precisão
print(f"The distance is: {distance:.3e} meters.")
# Saída: A distância é: 1.952e+05 metros.

# Notação científica com 6 dígitos de precisão
print(f"The distance is: {distance:.6e} meters.")
# Saída: A distância é: 1.952100e+05 metros.

# Quando você escreve números no código, você não usa vírgulas para separar os agrupamentos de dígitos (em outras palavras, você não escreve: 10.000.000, apenas 10000000). Recentemente, o Python adicionou uma notação que permite digitar usando sublinhados como 10_000_000. Em qualquer caso, quando você quiser exibir números grandes para o usuário, convém exibi-lo com vírgulas ou sublinhados. Isso é feito usando um ou após o nome da variável.:,:_

big_number = 123456789

# Display sem formatação:
print(f"The number is: {big_number}")
# Saída: O número é: 123456789

# Display com a formatação ",":
print(f"The number is: {big_number:,}")
# Saída: O número é: 123,456,789

# Display com a formatação "_":
print(f"The number is: {big_number:_}")
# Saída: O número é: 123_456_789

# Uma das coisas que torna possível escrever programas grandes e complexos é fazer uso de código pré-existente escrito por outras pessoas. Quando alguém agrupa partes de seu código para disponibilizá-lo para outras pessoas, ele é chamado de biblioteca. Em cursos futuros, você aprenderá sobre isso com muito mais detalhes, incluindo como fazer suas próprias bibliotecas. Python vem com muitas bibliotecas embutidas. Uma delas é chamada de biblioteca "Matemática", e contém funções e operações matemáticas comuns. Para usar o código dessa biblioteca em seu programa, você precisará importá-lo ou incluí-lo. Você faz isso colocando o código na parte superior do seu programa. Por exemplo, se você quiser usar o valor de Pi incluído na biblioteca matemática, faça o seguinte:"import math"

import math

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area}")
# Saída: A área é: 78.53981633974483

# Como era de se esperar, há muitas coisas disponíveis na biblioteca de matemática. Você pode ver a lista de funções matemáticas na documentação oficial. Se você é um cientista ou engenheiro, você vai querer se familiarizar com muitas dessas funções. Alguns que podem ser de seu interesse são os seguintes:

# math.ceil(value)—Arredonda para o próximo número inteiro, o "teto".value
# math.floor(value)—Arredonda para o próximo número inteiro.value
# math.exp(value)—Eleva-se ao poder de .value
# math.sin(value)—Calcula a função senoidal da trigonometria de em radianos.value

# Por exemplo:

import math

weight = 1.65

lower = math.floor(weight)
print(lower)
# Saída: 1

higher = math.ceil(weight)
print(higher)
# Saída: 2

# Por fim, uma nota sobre o bom estilo. Sempre que você escreve um programa, você precisa estar ciente do fato de que seu programa precisará ser compreendido e potencialmente reutilizado ou modificado por outros no futuro. Ele pode ser usado por outras pessoas da sua equipe, ou futuros funcionários da empresa, ou pode ser simplesmente você retornando ao seu programa depois de alguns meses, tentando se lembrar do que você fez. Além disso, escrever código limpo e bem formatado ajudará você a evitar bugs e problemas em seus programas enquanto você os escreve. Por esses motivos, é importante seguir boas práticas de nomear variáveis e formatar seu código. A maioria das empresas tem um guia de estilo rigoroso que o código deve seguir, mas em qualquer caso, é importante escrever código claro consistente. Você continuará a aprender mais sobre estilo neste e nos próximos cursos. Mas, neste ponto, aqui estão algumas diretrizes para ter em mente:

# Os nomes das variáveis devem ser significativos e descritivos. Nomes como "cnt" em vez de "count" ou "a" em vez de "area" serão mais difíceis de usar mais tarde.

# As variáveis devem estar todas em minúsculas com sublinhados separando palavras, como: , ou ._primary_songfirst_nametotal_page_count

# Inclua um espaço antes e depois dos operadores:

# Estilo adequado
# area = length * width

# Maus exemplos:
# area=length*width
# area= length * width
# area = length*width
# area = length *width

# Use linhas em branco para separar blocos do seu código que são semelhantes. Quando você escreve um artigo em inglês, você o divide em parágrafos compostos por várias frases que pertencem juntas. Da mesma forma, quando você escreve programas, geralmente tem três ou quatro linhas juntas e, em seguida, uma linha em branco antes do próximo grupo de três ou quatro. O importante aqui não é o número de linhas, mas sim separar o código em grupos que se relacionam entre si.

