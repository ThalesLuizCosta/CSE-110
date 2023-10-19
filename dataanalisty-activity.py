# Read data from the file
with open('data.txt', 'r') as file:
    lines = file.readlines()

# Convert lines to integers
ages = [int(line.strip()) for line in lines]

# Calculate the average age
average_age = sum(ages) / len(ages)

print(f"Average age: {average_age:.2f}")

# Check which ages are above or below the average
above_average = [age for age in ages if age > average_age]
below_average = [age for age in ages if age < average_age]

print(f"Ages above the average: {above_average}")
print(f"Ages below the average: {below_average}")