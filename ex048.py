print('Valores ímpares e múltiplos de 3 entre 1 e 500')
soma = 0
for c in range(0, 500):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print(soma)