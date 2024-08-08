m = 'S'
v = 0
c = 0
md = 0
maior = 0
menor = 0
while m != 'N':
    v = int(input('Informe um valor: '))
    if c == 0:
        maior = v
        menor = v
    else:
        if v > maior:
            maior = v
        elif v < menor:
            menor = v
    c += 1
    md += v
    m = str(input('Deseja continuar? [S/N]: '))
    if m == 'n':
        m = 'N'
print('Quantidade de valores digitados: {}\nMaior valor digitado: {}\nMenor valor digitado: {}\nMédia entre os valores digitados: {:.0f}'.format(c, maior, menor, md / c))