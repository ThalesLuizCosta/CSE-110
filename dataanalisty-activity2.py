"""
This program analyzes statistical data for different countries and years.
It reads data from a dataset, calculates averages for a specific year,
and finds the minimum and maximum values along with their corresponding countries
for a given year. The program handles the dataset by iterating through it line by line,
splits each line into parts, and computes the required statistics based on user input.
"""

# Read data from the dataset (assuming data is in a file named 'dataset.txt')
with open('countries.txt', 'r') as file:
    # Skip the header line
    next(file)

    # Initialize variables for highest and lowest values
    highest_value = float('-inf')
    lowest_value = float('inf')
    highest_country = ""
    lowest_country = ""

    # Initialize variables for average calculation
    total = 0
    count = 0

    # Iterate through the dataset
    for line in file:
        country, year, value = line.strip().split(',')
        value = float(value)

        # Find highest and lowest values along with their countries
        if value > highest_value:
            highest_value = value
            highest_country = country
        if value < lowest_value:
            lowest_value = value
            lowest_country = country

        # Calculate total for average
        total += value
        count += 1

    # Calculate average for all years
    average = total / count

    # User input for a specific year
    target_year = input("Enter a year: ")

    # Initialize variables for specific year calculations
    year_total = 0
    year_count = 0
    year_min_value = float('inf')
    year_max_value = float('-inf')
    year_min_country = ""
    year_max_country = ""

    # Iterate through the dataset for the specific year
    file.seek(0)  # Reset file pointer to the beginning of the file
    next(file)  # Skip the header line
    for line in file:
        country, year, value = line.strip().split(',')
        value = float(value)
        if year == target_year:
            # Calculate total for specific year average
            year_total += value
            year_count += 1

            # Find minimum and maximum values along with their countries for the specific year
            if value < year_min_value:
                year_min_value = value
                year_min_country = country
            if value > year_max_value:
                year_max_value = value
                year_max_country = country

    # Calculate average for the specific year
    if year_count > 0:
        year_average = year_total / year_count
    else:
        year_average = 0

    # Display results
    print(f"Highest Value: {highest_value} (Country: {highest_country})")
    print(f"Lowest Value: {lowest_value} (Country: {lowest_country})")
    print(f"Average for All Years: {average:.2f}")
    print(f"Minimum Value for {target_year}: {year_min_value} (Country: {year_min_country})")
    print(f"Maximum Value for {target_year}: {year_max_value} (Country: {year_max_country})")
    print(f"Average for {target_year}: {year_average:.2f}")