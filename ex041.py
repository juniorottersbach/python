yea = int(input('Informe o ano de nascimento do competidor: '))
if 2024 - yea < 10:
    print('Atleta mirim')
elif 2024 - yea < 15:
    print('Atleta infantil')
elif 2024 - yea < 20:
    print('Atleta junior')
elif 2024 - yea < 21:
    print('Atleta sênior')
else:
    print('Atleta master')