print('Informe o peso de 5 pessoas...')
pesoP = 0
pesoMaior = 0 
pesoMenor = float()
for c in range(1, 6):
    pesoP = float(input('Informe o peso da pessoa {}: '.format(c)))
    if c == 1:
        pesoMaior = pesoP
        pesoMenor = pesoP
    else:
        if pesoP > pesoMaior:
            pesoMaior = pesoP
        elif pesoP < pesoMenor:
            pesoMenor = pesoP
print('Das pessoas que foram pesadas\nA mais pesada pesa: {:.1f}Kg\nA mais leve pesa: {:.1f}Kg'.format(pesoMaior, pesoMenor))