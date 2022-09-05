real = float(input("Quanto você tem a carteira? R$ "))

dolar = real / 5.18
euro = real / 5.18
iene = real / 26.44

print(f"Com R$ {real:.2f} você pode comprar US$ {dolar:.2f}.")
print(f"Com R$ {real:.2f} você pode comprar {euro:.2f} €.")
print(f"Com R$ {real:.2f} você pode comprar ¥ {iene:.2f}.")