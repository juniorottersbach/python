nome = []
idade = []
sexo = []

idadeTotal = 0
homemMaisVelho = None
iddHomemMaisVelho = 0
qtdMulher20 = 0
for c in range(1, 5):
    print('Pessoa {}: '.format(c))
    nom = str(input('Informe o nome: '))
    idd = int(input('Informe a idade: '))
    sex = str(input('Informe o sexo (M/F): ')).upper().strip()
    nome.append(nom)
    idade.append(idd)
    sexo.append(sex)

    idadeTotal += idd

    if sex == 'M':
        if idd > iddHomemMaisVelho:
            iddHomemMaisVelho = idd
            homemMaisVelho = nom
    elif sex == 'F' and idd < 20:
        qtdMulher20 += 1

idadeMedia = idadeTotal / 4

print('Média de idade: {:.0f}'.format(idadeMedia))
if homemMaisVelho:
    print('{} é o homem mais velho e tem {} anos.'.format(homemMaisVelho, iddHomemMaisVelho))
else:
    print('Não foram inseridos homens.')
if qtdMulher20 > 0:
    print('Quantidade de mulheres com menos de 20 anos: {}.'.format(qtdMulher20))
else:
    print('Nenhuma mulher com menos de 20 anos foi adicionada na lista.')