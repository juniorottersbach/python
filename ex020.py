from random import randint
nome = []
nome.append(str(input("Digite o nome do aluno 1: ")))
nome.append(str(input("Digite o nome do aluno 2: ")))
nome.append(str(input("Digite o nome do aluno 3: ")))
nome.append(str(input("Digite o nome do aluno 4: ")))
print("Aluno escolhido: {}.".format(nome[randint(0,3)]))