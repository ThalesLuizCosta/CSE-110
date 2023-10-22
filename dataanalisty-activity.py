# Read data from the file
with open('datas.txt', 'r') as file:
    # Skip the header line using next()
    next(file)
    
    # Read data and convert commas to periods
    data = [float(line.strip().replace(",", ".")) for line in file]

# Find the maximum and minimum numbers
maximum_number = max(data)
minimum_number = min(data)

print(f"Maximum number: {maximum_number}")
print(f"Minimum number: {minimum_number}")

# Continue with the rest of your analysis code here