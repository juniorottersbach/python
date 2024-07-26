from random import choice
lista = []
lista.append(input("Primeiro aluno: "))
lista.append(input("Segundo aluno: "))
lista.append(input("Terceiro aluno: "))
lista.append(input("Quarto aluno: "))
print("O aluno escolhido foi: {}.".format(choice(lista)))