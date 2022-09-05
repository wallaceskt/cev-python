preco = float(input("Preço: "))

# Cálculo dos 5% do preço: preco * 5 / 100

novoPreco = preco - (preco * 5 / 100)

print(f"Preço antigo: R$ {preco:.2f}\nNovo preço: R$ {novoPreco:.2f} (5% de desconto)")