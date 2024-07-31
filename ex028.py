from random import randint
guess = randint(0, 5)
choice = int(input('Chute um número entre 0 e 5: '))
if choice < 0 or choice > 5:
    print('Informe um valor dentro do intervalo 0-5')
elif choice == guess:
    print('Computador: {}'.format(guess))
    print('Seu chute: {}'.format(choice))
    print('Você acertou')
else:
    print('Computador: {}'.format(guess))
    print('Seu chute: {}'.format(choice))
    print('Você errou')