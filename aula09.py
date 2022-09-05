frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(frase.replace('Python', 'Javascript'))

frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())

dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

frase = '   Curso em Vídeo Python  '
print(len(frase.strip()))

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse at eros a neque pharetra convallis. 
Praesent accumsan massa sed magna finibus, et semper quam auctor. Etiam venenatis, sem at ultricies semper, mi purus luctus nisi, et commodo felis sapien a tellus.""")