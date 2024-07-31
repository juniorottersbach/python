sal = float(input('Informe seu salário: '))
if sal <= 1250:
    print('Salário reajustado: R$ {:.2f}'.format(sal*1.15))
else:
    print('Salário reajustado: R$ {:.2f}'.format(sal*1.10))