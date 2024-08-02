age = int(input('Informe sua idade: '))
if age < 18:
    print('Você deverá se alistar em {} anos.'.format(18 - age))
elif age > 18:
    print('Você deveria ter se alistado {} anos atrás.'.format(age - 18))
else:
    print('Você tem a idade correta, deve se alistar esse ano.')