# Usar um loop for e o comprimento da cadeia de caracteres é uma maneira padrão de acessar o índice e a letra. No entanto, o Python também tem uma maneira de acessar essas duas variáveis diretamente usando uma função especial chamada como mostrado no exemplo a seguir: "enumerate".

first_name = "Thales"

for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")

# note que usando o "enumerate", nós especificamos ambos "i" e "letter".
# Isso é um pouco diferente do loop padrão, porque ele retorna duas variáveis. Esta função não é suportada em muitas linguagens, mas está disponível em Python e você está convidado a usá-la em seus programas, se quiser.