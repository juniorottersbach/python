year = int(input('Informe um ano para descobrir se é bissexto: '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('É bissexo')
else:
    print('Não é bissexto')