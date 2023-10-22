"""
This program analyzes statistical data for different countries and years. It reads data from a database file, calculates averages for a specific year, and finds the minimum and maximum values along with their corresponding countries for a given year.
"""

# Read data from the file
with open('dados.txt', 'r') as file:
    # Skip the header line
    next(file)

    # Parse data and store in a list of tuples (country, year, statistic)
    data = [line.strip().split(',') for line in file]

# Loop para solicitar dados até que dados válidos sejam inseridos
while True:
    # Ano e país inseridos pelo usuário
    target_year = int(input("Enter a year: "))
    target_country = input("Enter a country: ")

    # Flag para verificar se os dados foram encontrados
    data_found = False

    # Calcular média para o ano fornecido
    total = 0
    count = 0
    for country, year, value in data:
        if int(year) == target_year and country.lower() == target_country.lower():
            total += float(value)
            count += 1
            data_found = True

    if data_found:
        average = total / count
        print(f"Average statistic for {target_country}, {target_year}: {average:.2f}")
        
        # Encontrar valores mínimos e máximos e países correspondentes para o ano fornecido
        min_value = float('inf')
        max_value = float('-inf')
        min_country = ""
        max_country = ""

        for country, year, value in data:
            if int(year) == target_year:
                if float(value) < min_value:
                    min_value = float(value)
                    min_country = country
                if float(value) > max_value:
                    max_value = float(value)
                    max_country = country

        print(f"Minimum statistic for {target_country}, {target_year}: {min_value} (Country: {min_country})")
        print(f"Maximum statistic for {target_country}, {target_year}: {max_value} (Country: {max_country})")
        break  # Sai do loop se os dados válidos foram encontrados
    else:
        print("No data found for the given year or country. Please try again.")
        # Continua pedindo novamente os dados
        continue
