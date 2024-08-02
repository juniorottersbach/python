n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
if (n1 + n2) / 2 < 5:
    print('REPROVADO')
elif (n1 + n2) / 2 <= 6.9:
    print('RECUPERAÇÃO')
else: 
    print('APROVADO')