# Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcular e mostrar o comprimento da hipotenusa
from math import hypot

catOposto = int(input("Cateto oposto: "))
catAdjacente = int(input("Cateto adjacente: "))

# fórmula de pitágoras: a2 + b2 = c2 ou
# hipo = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)
hipo = hypot(catOposto, catAdjacente)

print(f'A hiponetusa é: {hipo:.2f}.')