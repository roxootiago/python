from random import shuffle

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

alunos = [aluno1,aluno2,aluno3,aluno4]
shuffle(alunos)

for i in range (len(alunos)):
    print(alunos[i],end = " ")