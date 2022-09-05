# Ler número Real qualquer pelo teclado e mostrar sua porção inteira. Ex.: 6.127 -> 6
from math import trunc

num = float(input("Digite um número: "))

# print(f'A parte inteira de {num} é {num:.0f}.')
# print(f'A parte inteira de {num} é {int(num)}.')
print(f'A parte inteira de {num} é {trunc(num)}.')