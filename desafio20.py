# Um professor quer sortear a ordem de apresentação dos seus quatro alunos e mostre a ordem sorteada
import random

alunos = []

a1 = str(input("Nome do aluno 1: "))
alunos.append(a1)
a2 = str(input("Nome do aluno 2: "))
alunos.append(a2)
a3 = str(input("Nome do aluno 3: "))
alunos.append(a3)
a4 = str(input("Nome do aluno 4: "))
alunos.append(a4)

# alunos = ['Wallace', 'Fernanda', 'Luana', 'Aline']
# Pode usar .append() ou apenas:
# alunos = [a1, a2, a3, a4]

random.shuffle(alunos)

print('Ordem de apresentação:')
for i in alunos:
    print(i)