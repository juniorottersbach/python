print('Desenvolva um programa que receba um número e devolva sua tabuada')
n = int(input('Digite o valor: '))
for x in range(1, 11):
    print('{} x {} = {}'.format(n, x, n*x))