from random import randint
pc = randint(1,10)
c = 0
i = 0
l = 0
print('Tente adivinhar o número que o computador pensou (entre 1 e 10)')
while l != 33:
    c = int(input('Qual seu palite?: '))
    i += 1
    if c == pc:
        l = 33
print('Você acertou em {} tentativas'.format(i))