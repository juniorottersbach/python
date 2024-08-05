print('Informe 6 valores...')
val = 0
soma = 0
for c in range(1, 7):
    val = int(input('Valor {}: '.format(c)))
    if val % 2 == 0:
        soma += val
print('Soma dos valores pares: {}'.format(soma))