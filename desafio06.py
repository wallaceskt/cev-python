num = int(input("Digite um número: "))

dob = num * 2
tri = num * 3
rai = pow(num, (1/2)) # num ** (1/2)

# print("O dobro de {}: {}\nO triplo de {}: {}\nA raiz quadrada de {}: {:.2f}.".format(num, dob, num, tri, num, rai))
print(f"O dobro de {num}: {dob}\nO triplo de {num}: {tri}\nA raiz quadrada de {num}: {rai:.2f}.")