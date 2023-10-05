for name in ['Thales', 'Pamela']:
    print(name)

# no caso de "for", ele irá procurar os elementos que estão dentro de uma variável, como por exemplo "Thales e Pamela", para assim mostrar os dois nomes que estão dentro da lista de variáveis, mas se eu quiser repetir isso por um período X, eu adiciono a função chamada "range".

for index in range(0, 2):
    print(index)

# no exemplo acima pode parecer que ele fez a mesma coisa que o "while", mas neste caso a única diferença é que quando chamamos o "range", ele cria automaticamente aquele "array" de "0 e 1", se você quiser um loop com um determinado múmero de vezes, use o "range" para isso.

# agora no último loop que está disponível para nós é um "loop while", e com um "loop while" o que devemos especificar é alguma condição, portanto, desde que algo seja verdadeiro, no meu caso o índice seja menor que o comprimento, permaneceremos dentro desse "loop while", mas o agora o problema do "loop while" é que você precisa alterar a condição, em algum momento, isso precisa ser testado como falso, do contrário, você ficará preso lá para sempre e acabará recebendo um "erro de estouro de pilha", portanto, você precisa ter certeza de alterar a condição(como no caso abaixo)

names = ['Thales', 'Pamela']
index = 0
while index < len(names):
    print(names[index])
    # a condição foi alterada!!!
    index = index + 1