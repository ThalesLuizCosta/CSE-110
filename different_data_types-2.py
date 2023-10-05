# Isto cria uma nova interação variável com o valor 10
# Não há nenhuma mágica para o nome na variável "_num", isso só irá manter o valor da variável.

length_num = 50
width_num = 10

# Se você adicionar números juntos, você teria o seu resultado esperado:
print(length_num + width_num)
# This displays: 60

# Você pode converter valores para as strings "50" and "10" desta forma:
length_string = str(length_num)
width_string = str(width_num)

# O computador não irá pensar nessas variáveis como dois caracteres, o dígito 5 seguido do dígito 0, e o dígito 1 seguido pelo dígito 0.

# Se você tentar adicionar duas strings juntas, elas irão concatenatar, ou mostrar uma após a outra:
print(length_string + width_string)
# This displays: 5010