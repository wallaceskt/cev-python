# Ler o nome de uma cidade e informe se começa ou não com 'SANTO'
import math
nome = str(input('Cidade: ')).strip()

if (nome[:5].upper() == 'SANTO'):
    print(f'A cidade de {nome.upper()} começa com "SANTO".')
else:
    print(f'A cidade de {nome.upper()} NÃO começa com "SANTO".')