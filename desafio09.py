num = int(input("Digite um número: "))

itens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("-" * 20 + "\nADIÇÃO\n" + "-" * 20)

for item in itens:
    print("{} + {:2} = {}".format(num, item, num+item))

print("\n" + "-" * 20 + "\nSUBTRAÇÃO\n" + "-" * 20)

for item in itens:
    print("{} - {:2} = {}".format(num, item, num-item))

print("\n" + "-" * 20 + "\nMULTIPLICAÇÃO\n" + "-" * 20)

for item in itens:
    print("{} X {:2} = {}".format(num, item, num*item))

print("\n" + "-" * 20 + "\nDIVISÃO\n" + "-" * 20)

for item in itens:
    print("{:2} : {} = {:.0f}".format(item, num, item/num))