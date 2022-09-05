# Ler uma frase e mostre: quantas vezes aparece a letra 'A', em que posição ela aparece a primeira vez e em que posição ela aparece a última
frase = str(input('frase: ')).upper().strip()

letra = frase.count('A')
primeira = frase.find('A')
ultima = frase.rfind('A')

print(f'Frase: "{frase}"')
print(f'A letra "a" aparece {letra} vez(es).')
print(f'A primeira ocorrência da letra "A" está na posição: {primeira}.')
print(f'A última ocorrência da letra "A" está na posição: {ultima}.')