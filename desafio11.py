largura = float(input("Largura da parede (m): "))
altura = float(input("Altura da parede (m): "))

area = largura * altura
qtdTinta = area / 2

print(f"A quantidade de tinta para pintar {area} m2 de parede é de {qtdTinta} l de tinta.")