algo = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É numérico? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Esta totalmente maiúsculo? {}'.format(algo.isupper()))
print('Esta totalmente minúsculo? {}'.format(algo.islower()))
print('Esta em capital? {}'.format(algo.istitle()))