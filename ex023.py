num = int(input('Informe um valor entre 0 e 9999: '))
if (num >= 0 & num <= 9999):
    print('Numero informado {}'.format(num))
    print('unidade: {}'.format(num // 1 % 10))
    print('Dezena: {}'.format(num // 10 % 10))
    print('Centena: {}'.format(num // 100 % 10))
    print('Milhar: {}'.format(num // 1000 % 10))