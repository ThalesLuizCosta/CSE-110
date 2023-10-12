books = []

books.append("1 Nephi")
books.append("2 Nephi")
books.append("Jacob")
books.append("Enos")

number_of_books = len(books)

for i in range(len(books)):
    book = books[i]
    print(book) # mostra cada livro na tela.

    # Não esqueça que Python, como a maioria das linguagens de programação, começa a contar em 0 para seus índices. Portanto, o primeiro item está no índice 0 e o último item de uma lista de 10 elementos estaria no índice 9.

    # Nas lições anteriores, você aprendeu como iterar cada item de uma lista usando um loop for padrão, outra maneira de fazer isso é fazer com que o loop itere pelos índices 0 até o tamanho da lista.