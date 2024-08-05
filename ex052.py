num = int(input('Informe um valor para saber é simples ou composto: '))
cont = 0
for c in range(2, num+1):
    if num % c == 0:
        cont += 1
if cont == 1:
    print('{} é primo'.format(num))
elif num == 1: 
    print('{} não é primo e nem composto'.format(num))
else:
    print('{} é composto'.format(num))
