# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
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

# alunos = [a1, a2, a3, a4]
# alunos = ['Wallace', 'Fernanda', 'Luana', 'Aline']

sorteado = random.choice(alunos)

print(f'O(A) sorteado(a) é {sorteado}.')