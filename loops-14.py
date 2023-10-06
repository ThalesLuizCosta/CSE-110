# no exemplo anterior supunha que o número de letras, ou o comprimento da cadeia de caracteres, seria sempre 4, mas isso não funcionará se a cadeia de caracteres tiver mais ou menos letras. Em vez de digitar o 4 diretamente, você pode deixar o computador encontrar o comprimento usando a função. O código a seguir mostra como usar para obter o comprimento de uma cadeia de caracteres, combinar a função com o loop anterior é muito poderoso, porque agora você pode iterar através dos índices e letras de cadeias de caracteres de qualquer comprimento da seguinte maneira: "len".

dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)

print(f"Your dog's name has {letter_count} letters")