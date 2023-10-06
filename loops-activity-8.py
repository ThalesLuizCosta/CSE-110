word = "Commitment"
favorite = input("What is your favorite letter? ")

for letter in word:
    # Caso a palavra ou letra do usuário contenha maiúscula, deve converter as letras para minúsculas quando as compararmos.
    if letter.lower() == favorite.lower():
        print("_", end="") # aqui ele substitui quando usado junto da variável o "end=", para que a letra não seja mostrada na saída.
    else:
        print(letter.lower(), end="")
print()