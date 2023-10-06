for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}")

# lembrando que o que for posto depois do for é o que deve ser inserido no "print", por exemplo o "i" é o que será colocado em função, fazendo assim a contagem, por isso ele é indicado o valor depois do "range" e depois colocado em função e por fim no "print".

# Observe como o loop interno "j" é executado toda vez que o loop externo "i" exibe seu número. Os loops internos podem ser muito úteis na iteração através de uma estrutura bidimensional, como os pixels de uma imagem.

# Embora geralmente prefiramos nomes de variáveis ​​que sejam mais descritivos do que uma única letra, se a variável for usada apenas para contagem em um loop simples, seu uso será considerado padrão. Então, se você tem um loop interno, você usa , e um terceiro loop interno seria. Se você tiver mais de três loops, você deve considerar se há uma maneira mais simples de realizar sua tarefa e, se realmente não houver, você deve pelo menos mover para nomes de variáveis mais descritivas nesse ponto.