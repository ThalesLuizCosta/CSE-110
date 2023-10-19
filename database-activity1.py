# NUNCA SE ESQUEÇA QUE O NOME DE UMA FUNÇÃO SERÁ MELHOR SE PARECER COM O NOME DO ARQUIVO.

with open("books.txt") as book_file: 
    for line in book_file:
    
        book = line.strip()

        print(book) # NUNCA SE ESQUEÇA QUE A IDENTAÇÃO FAZ DIFERENÇA!!!