# Ler uma frase e mostre se tem ou não 'SILVA'
nome = str(input('Nome: ')).strip()

if ('SILVA' in nome.upper()):
    print(f'{nome.upper()} tem "SILVA".')
else:
    print(f'{nome.upper()} NÃO tem "SILVA".')