hou = float(input('Informe o valor da casa: '))
sal = float(input('Informe o seu salário: '))
yea = int(input('Informe em quantos anos vai pagar: '))
if hou / (yea * 12) <= (sal * 0.3):
    print('Financiamento aprovado.')
else:
    print('Financiamento recusado pois excede 30% do seu salário.')