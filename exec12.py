S = input("Texto: ")
MA = 0
MI = 0

for L in S:
    # if(L.isupper()):
    if 'A' <= L <= 'Z':
        MA += 1
    # else:
    elif  'a' <= L <= 'z':
        MI += 1

print(f"Maiúsculas: {MA}\nMinúsculas: {MI}")