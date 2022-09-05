print("-" * 20)
print("\Aluguel de Carros\n")
print("-" * 20)

dias = float(input("Quantos dias alugados? "))
kms = float(input("Quantos km rodados? "))

carro = 60 # por dia
km = 0.15 # por km rodado
preco = (carro * dias) + (km * kms)

print(f"O preço a pagar é de R$ {preco:.2f}.")