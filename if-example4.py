price = 50.00

country = 'Canada'

province = float(input("How much it cost in " == price))

if province == 'Alberta':
    tax = 0.05
if province == 'Nunavut':
    tax = 0.05
if province == 'Ontario':
    tax = 0.13

    # Não é uma forma errada de fazer a verificação de qual provícia o imposto está sendo visto, mas existe uma ainda mais "elegante" para isso.

if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13

    # Quando se usa o "elif" está se dizendo para verificar sempre a próxima condição para ver se é aquilo que se é esperado ou se deverá procurar pela próxima, ou seja ele fará isso até achar o que procura, e quando ele achar ele irá parar ali mesmo. Portanto o "elif me permite fazer uma maneira um pouco mais eficiente de verificar o código", mas ATENÇÃO...ainda é preciso os dois pontos (:) no final de cada instrução.

if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15

    # Portanto, a outra vantagem de um "elif" é que posso ter essa ação tendo o "else" como padrão.

if province == 'Alberta' \
    or province == 'Nunavut' :
    # nesse caso quando é usado o "or" é sempre visto que o valor de uma função(no caso a taxa de imposto) servirá para calcular para (no caso) "Nunavut" ou "Alberta"
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15

    # A maneira como o "or"  funciona é se a primeira condição for verdadeira ou a segunda condição é verdadeira, então o resultado desta linha de julgamento é verdadeiro, a lógica do "or" é muito simples, contanto que qualquer condição seja verdadeira, o resultado será verdadeiro(ou no caso "TRUE").

    # No caso dos impostos de "Alberta" ou "Nunavut" estão fixados em 5%, mas se no caso for chamado a função diferente das provícias de "Alberta" ou "Nunavut" então o programa não irá chamar a próxima condição dentro de "or".

if province in('Alberta', \
               'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15

    # Se você tiver uma lista e se você quiser verificá-los um a um, na verdade existe uma sintaxe mais concisa nesse caso, você pode usar o operador "in", basicamente quando a situação é "if == a algo ou outra coisa", nesse caso você pode usar o operador "in". A lógica deste negócio é na verdade, assim como no mundo real, nestes três lugares no Canadá, todos têm a mesma alíquota de 5%. Então posso escrever "if province in():", os parâmetros de "in" são três províncias: Alberta, Nunavut e Yukon, contanto que o valor da variável "province" seja igual a qualquer uma destas três provícias, basta definir a taxa de imposto para 5%, você também pode usar o "or"(como descrito no exemplo acima) que o trabalho será feito de forma perfeita, mas ao usar o "in" torna o programa mais conciso, mas você pode decidir qual usar, basicamente existem duas maneiras de escrever.

    # Mas se no caso você estiver visitando o Canadáem uma viagem, não será cobrado imposto, então talvez precisemos dizer...

if country == 'Canada':
    if province in('Alberta', \
                   'Nunavut', 'Yukon'): 
        tax = 0.05 # Se você estiver no Canadá e se a província estiver nesta lista (Alberta, Nunavut ou Yukon), então seu imposto é de 5%.
    elif province == 'Ontario':
        tax = 0.13 # esses quatro espaços no início de cada linha realmente mudarão como o programa é executado, por isso tenha cuidado, especialmente quando você começa a aninhar uma camada após camada de instruções "if" aninhadas.
    else:
        tax = 0.15
else:
    tax = 0.0

    # Portanto usaremos a instrução "if" aninhadas, então aqui estou, existe uma declaração "if" e na declaração "if" existe outro "if", mas preste atenção ao "if" dentro, também existem recuos que existem quatro espaços na frente dele, isso não faz com que pareça mais legível, mas isso faz com que mais código fique mais legível, mas o recuo será prático e afetará a execução do programa, lembre-se...não importa o que esteja dentro, enquanto tiver o recuo, as linhas serão apenas recuadas, só será executado se a condição "if" anterior for atendida, então toda essa declaração "if" está no código para determinar diferentes taxas de impostos com base na província e só seá executado se o endereço público for "Canada".

    # Aqui pode estar um que você pensa onde você pode usar funções ou onde isso pode ser evitado quando ocorreu um erro no recuo, mas a boa notícia é que estamos prestes a aprensentar a função.