num = '1234'
num = str(input('Informe um valor entre 0000 e 9999: '))
print('Numero informado {}'.format(num))
print('unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))