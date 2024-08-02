from random import randint
from time import sleep
dec = int(input('Jogo de PEDRA-PAPEL-TESOURA\n1 para PEDRA\n2 para PAPEL\n3 para TESOURA\nQual sua decisão?: '))
comp = randint(1,3)
sleep(2)
if dec == 1 and comp == 1:
    print('Jogador: Pedra\nComputador: Pedra\nEMPATE')
elif dec == 1 and comp == 2:
    print('Jogador: Pedra\nComputador: Papel\nVITÓRIA DO COMPUTADOR')
elif dec == 1 and comp == 3:
    print('Jogador: Pedra\nComputador: Tesoura\nVITÓRIA DO JOGADOR')
elif dec == 2 and comp == 1:
    print('Jogador: Papel\nComputador: Pedra\nVITÓRIA DO JOGADOR')
elif dec == 2 and comp == 2:
    print('Jogador: Papel\nComputador: Papel\nEMPATE')
elif dec == 2 and comp == 3:
    print('Jogador: Papel\nComputador: Tesoura\nVITÓRIA DO COMPUTADOR')
elif dec == 3 and comp == 1:
    print('Jogador: Tesoura\nComputador: Pedra\nVITÓRIA DO COMPUTADOR')
elif dec == 3 and comp == 2:
    print('Jogador: Tesoura\nComputador: Papel\nVITÓRIA DO JOGADOR')
elif dec == 3 and comp == 3:
    print('Jogador: Tesoura\nComputador: Tesoura\nEMPATE')
else:
    print('Escolha uma opção válida.')