# Ler o nome da pessoa e mostrar: nome com letras maiúsculas, nome com letras minúsculas, quantas letras sem contar os espaços e quantas letras tem o primeiro nome
nome = str(input('Nome: '))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
dividido = nome.split()
print(str(dividido[0]) + ' - ' + str(len(dividido[0])))
