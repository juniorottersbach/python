tab = int(input('Informe o valor que deseja saber a tabuada: '))
for c in range(0, 101):
    print('{}x{} = {}'.format(tab, c, tab * c))