word = "Commitment"
favorite = input("What is your favorite letter? ")

for letter in word:
    # Caso a palavra ou letra do usuário contenha maiúscula, deve converter as letras para minúsculas quando as compararmos
    if letter.lower() == favorite.lower():
        print(letter.upper(), end='')
    else:
        print(letter.lower(), end='')
print ()
print(f"Your favorite letter is {favorite}")