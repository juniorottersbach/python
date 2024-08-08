x = 0
c = 0
s = 0
i = 0
while c != 999:
    x = int(input('Digite um valor [999 para sair]: '))
    if x == 999:
        c = 999
    else:
        s += x
        i += 1
print('Quantidade de valores digitados: {}\nSoma dos valores digitados: {}'.format(s, i))