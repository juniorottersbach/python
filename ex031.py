dist = int(input('Informe a distância da viagem: '))
if dist < 1:
    print('Informe um valor válido')
elif dist < 200:
    print('Valor da passagem: R$ {:.2f}'.format(dist * 0.5))
else:
    print('Valor da passagem: R$ {:.2f}'.format(dist * 0.45))