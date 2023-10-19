
with open('cities.txt') as archive:
    # Lê as linhas do arquivo
    lines = archive.readlines()

# Inicializa as variáveis para os valores mais altos e mais baixos
higher_value = 0  # Inicializado com um valor negativo infinito
lower_value = 1000000000  # Inicializado com um valor positivo infinito

# Itera pelas linhas do arquivo
for line in lines:
    # Divide a linha em partes usando espaço como delimitador (altere para o delimitador correto)
    parts = line.split()
    
    # Trata a primeira linha (se necessário)
    if lines.index(line) == 0:
        # Trate a primeira linha aqui
        pass
    
    # Itera pelas partes da linha
    for part in parts:
        # Converte a parte para um número (assumindo que são números)
        number = float(part)
        
        # Atualiza o valor mais alto, se necessário
        if number > higher_value:
            higher_value = number
        
        # Atualiza o valor mais baixo, se necessário
        if number < lower_value:
            valor_mais_baixo = number

# Exibe os valores mais altos e mais baixos
print(f"Valor mais alto: {higher_value}")
print(f"Valor mais baixo: {lower_value}")