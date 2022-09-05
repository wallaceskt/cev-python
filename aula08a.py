# Exemplo importando toda a biblioteca math
# import math

# num = int(input('Digite um número: '))

# raiz = math.sqrt(num)

# print(f'A raiz quadrada de {num} é igual a {raiz:.2f}.')

# ---------- #

# Exemplo importando apenas a função sqrt de math
# from math import sqrt

# num = int(input('Digite um número: '))

# raiz = sqrt(num)

# print(f'A raiz quadrada de {num} é igual a {raiz:.2f}.')

# ---------- #

# Exemplo importando duas funções de math
# from math import sqrt, floor

# num = int(input('Digite um número: '))

# raiz = sqrt(num)

# print(f'A raiz quadrada de {num} é igual a {floor(raiz)}.')

# ---------- #

# Importando a biblioteca random
import random

# random() gera um número aleatório entre 0 e 1
# num = random.random()

# randint() gera um número aleatório inteiro entre dois números
num = random.randint(1, 10)

print(num)

# ---------- #

# import emoji

# print(emoji.emojize("Olá, Mundo :sunglasses", use_aliases=True))