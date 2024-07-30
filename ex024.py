city = str(input('Informe o nome de uma cidade: ')).strip()
first = city.split()
if (first[0].upper().find('SANTO') > 0):
    print('O nome de sua cidade começa com Santo')
else:
    print('O nome de sua cidade não começa com Santo')