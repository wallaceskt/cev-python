print("-" * 20)
print("\nConversor de temperatura\n")
print("-" * 20)

tempC = float(input("Temperatura: ºC "))

tempF = (tempC * 1.8) + 32 # ((9 * tempC) / 5) +32
tempK = tempC + 273

print(f"{tempC:.2f} ºC é igual a {tempF:.1f} ºF.")
print(f"{tempC:.2f} ºC é igual a {tempK:.1f} K.")