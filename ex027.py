name = str(input('Digite seu nome completo: ')).strip()
name = name.title().split()
print('Seu primeiro nome: {}'.format(name[0]))
print('Seu último nome: {}'.format(name[len(name)-1]))