n = int(input('Quantos números quer saber da sequência de fibonacci: '))
c = 0
lista = [0,1]
while c != n:
   c += 1
   lista.append(lista[c - 1] + lista[c])
print(lista)