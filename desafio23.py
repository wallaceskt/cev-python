# Ler um número de 0 a 9999 e mostrar cada um dos números separados
# Ex.: 1234
# unidade: 4
# dezena: 3
# centena 2
# milhar: 1

# import math
num = int(input('Número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: ' + str(u))
print('dezena: ' + str(d))
print('centena: ' + str(c))
print('milhar: ' + str(m))

# dividido = [num//(10**i)%10 for i in range(math.ceil(math.log(num, 10)) -1, -1, -1)]
# dividido = [int(a) for a in str(num)]
# print(dividido)
# if (len(dividido) == 4):
#         print('unidade: ' + str(dividido[3]))
#         print('dezena: ' + str(dividido[2]))
#         print('centena: ' + str(dividido[1]))
#         print('milhar: ' + str(dividido[0]))
# elif (len(dividido) == 3):
#         print('dezena: ' + str(dividido[2]))
#         print('centena: ' + str(dividido[1]))
#         print('milhar: ' + str(dividido[0]))
# elif (len(dividido) == 2):
#         print('centena: ' + str(dividido[1]))
#         print('milhar: ' + str(dividido[0]))
# elif (len(dividido) == 1):
#         print('centena: ' + str(dividido[0]))