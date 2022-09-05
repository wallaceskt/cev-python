# d = int(input("Depositar: "))
# s = int(input("Sacar: "))
# s = int(input("Sacar: "))

valor = 0

while True:
    entrada = input()
    C, N = entrada.split(" ")

    if(C == "D"):
        valor += int(N)
    elif(C == "S"):
        valor -= int(N)
    else:
        break

print(valor)