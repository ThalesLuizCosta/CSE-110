first_num = '5'
second_num = '6'
print(first_num + second_num)
# aqui o python irá entender que são strings e não numerais, por isso os colocou lado a lado.
first_num = input('Enter the first number ')
second_num = input('Enter the second number ')
print(first_num + second_num)
# assim como no primeiro exemplo, ele entenderá com essa forma que você quer colocar os números lado a lado.
first_num = input('Enter the first number ')
second_num = input('Enter the second number ')
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))