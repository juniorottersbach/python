from random import shuffle
lista = []
lista.append(input("Primeiro aluno: "))
lista.append(input("Segundo aluno: "))
lista.append(input("Terceiro aluno: "))
lista.append(input("Quarto aluno: "))
shuffle(lista)
print("A ordem de apresentação é: ")
print(lista)