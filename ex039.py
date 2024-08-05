from datetime import date
atual = date.today().year
age = int(input('Informe seu ano de nascimento: '))
idade = atual - age
if idade < 18:
    print('Você deverá se alistar em {} anos.'.format(18 - idade))
elif idade > 18:
    print('Você deveria ter se alistado {} anos atrás.'.format(idade - 18))
else:
    print('Você tem a idade correta, deve se alistar esse ano.')