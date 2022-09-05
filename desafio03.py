n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
p = input("Somar? ")
# def soma(n1, n2):
#     return n1 + n2

# print("A soma de " + str(n1) + " e " + str(n2) + " é %d" %soma(n1, n2))

soma = n1 + n2
multi = n1 * n2
divi = n1 / n2
divt = n1 // n2
expo = n1 ** n2
# print("A soma de " + str(n1) + " e " + str(n2) + " é", soma)
# print("A soma de {} e {} é {}".format(n1, n2, soma))
print(type(n1))
print(type(n2))
# O método isnumeric() diz se é possível converter o valor em um número ou em um tipo primitivo int
print(p.isnumeric())
# O método isalpha() diz se é letra
print(p.isalpha())
# O método isalpha() diz se é alfanumérico
print(p.isalnum())
print(p.isdecimal())
# print("A soma de {0} e {1} é {2}".format(n1, n2, soma))
# print("A soma de {0} e {1} é {2}".format(n1, n2, n1+n2))
print("A soma é {}\nO produto é {}\nA divisão é {:.3f}\nA divisão inteira é {}\nA potência é {}".format(soma, multi, divi, divt, expo))

if p.isnumeric():
    print("O valor {} é numérico.".format(p))
elif p.isalpha():
    print("O valor {} é alfa.".format(p))
else:
    print("O valor {} não é numérico nem alfa.".format(p))
