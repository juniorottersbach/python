from datetime import date
print('Informe a idade de 7 pessoas...')
anoA = date.today().year
idade = 0
contMaior = 0
contMenor = 0
for c in range(1, 8):
    idade = int(input('Informe o ano de nascimento da pessoa {}: '.format(c)))
    if (anoA - idade) >= 21:
        contMaior += 1
    else:
        contMenor += 1
print('Das pessoas informadas: {} atingiram a maioridade e {} ainda não atingiram a maioridade.'.format(contMaior, contMenor))