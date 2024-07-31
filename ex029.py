speed = int(input('Informe a velocidade do veículo: '))
if speed >= 80:
    print('O veículo foi multado no valor: R$ {:.2f}'.format((speed - 80) * 7))
else:
    print('O veículo não foi multado')