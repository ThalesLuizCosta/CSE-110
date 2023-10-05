age = int(input('How old are you? '))
next_year_age = age + 1
print(f'On my next birthday, I will be {next_year_age}.')
print()
cartons = int(input('How many egg cartons do you have? '))
eggs = cartons * 12
print(f'You have {eggs} eggs')

# No próximo exemplo, para criar uma linha em branco incluí \n no início da string
cookies = int(input('\nHow many cookies do you have? '))
people = int(input('How many people are there? '))

cookies_per_person = cookies / people

print(f'Each person may have {cookies_per_person} cookies')