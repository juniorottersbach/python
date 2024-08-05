print('Verificador de palíndromo')
frase = str(input('Informe uma frase: ')).replace(" ","")
fraseR = frase[::-1]
cont = 0
for c in range(len(str1) -1, -1, -1):
    if str1[c] == str2[c]:
        cont += 1
if cont == len(str1):
    print('{} é palíndroma'.format(str1))
else:
    print('{} não é palíndroma'.format(str1))