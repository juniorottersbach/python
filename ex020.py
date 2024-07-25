import random
nome = []
nome.append(str(input("Digite o nome do aluno 1: ")))
nome.append(str(input("Digite o nome do aluno 2: ")))
nome.append(str(input("Digite o nome do aluno 3: ")))
nome.append(str(input("Digite o nome do alone 4: ")))
print("Aluno escolhido: {}.".format(nome[random.randint(0,3)]))