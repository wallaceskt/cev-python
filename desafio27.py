# Ler o nome completo de uma pessoa e mostre: o primeiro e o último nome separadamente
# Ex.: Wallace de Oliveira Sales
# primeiro = Wallace
# último = Sales
nome = str(input('nome: ')).strip()

palavra = nome.split()
primeira = palavra[0]
ultima = palavra[len(palavra) - 1]

print(f'primeiro = {primeira}')
print(f'último = {ultima}')