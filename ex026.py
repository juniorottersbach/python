phrase = str(input('Escreva uma frase qualquer: ')).strip()
qntA = phrase.upper().count('A')
print('Quantidade de As na sua frase: {}'.format(qntA))
firstA = phrase.upper().find('A') + 1
print('Primeira letra A é na posição: {}'.format(firstA))
lastA = phrase.upper().rfind('A') + 1
print('Última letra A é na posição: {}'.format(lastA))