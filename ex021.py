from random import randint
nome = []
nome.append(str(input("Digite o nome do aluno 1: ")))
nome.append(str(input("Digite o nome do aluno 2: ")))
nome.append(str(input("Digite o nome do aluno 3: ")))
nome.append(str(input("Digite o nome do alone 4: ")))
print("Ordem de apresentação:")
aluno = randint(0, len(nome)-1)
print("Primeiro grupo: {}.".format(nome[aluno]))
nome.pop(aluno)
aluno = randint(0, len(nome)-1)
print("Segundo grupo: {}.".format(nome[aluno]))
nome.pop(aluno)
aluno = randint(0, len(nome)-1)
print("Terceiro grupo: {}.".format(nome[aluno]))
nome.pop(aluno)
aluno = randint(0, len(nome)-1)
print("Quarto grupo: {}.".format(nome[aluno]))
nome.pop(aluno)