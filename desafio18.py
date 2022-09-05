# Ler um ângulo qualquer e mostrar na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan

angulo = float(input("Ângulo (º): "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O seno de {radians(angulo)} rad é: {seno:.2f}.\nO cosseno {radians(angulo)} rad é: {cosseno:.2f}\nA tangente {radians(angulo)} rad é: {tangente:.2f}')