nome = str(input('Digite seu nome: '))
print('Seu nome maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
frase = nome.split()
nome = ''.join(frase)
print('Quantidade de letras em seu nome: {}'.format(len(nome)))
print('Quantidade de letras em seu primeiro nome: {}'.format(len(frase[0])))