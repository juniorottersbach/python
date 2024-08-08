num1 = int(input('Informe um valor: '))
num2 = int(input('Informe outro valor: '))
maior = 0
7
c = 0
while c != 5:
    c = int(input('Opções:\n[1] para somar\n[2] para multiplicar\n[3] para saber o maior\n[4] para novos valores\n[5] para sair\nEscolha: '))
    if c == 1:
        print('A soma entre {} e {} é {}'.format(num1, num2, num1 + num2))
    elif c == 2:
        print('O produto entre {} e {} é {}'.format(num1, num2, num1 * num2))
    elif c == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior valor entre {} e {} é {}'.format(num1, num2, maior))
    elif c == 4:
        num1 = int(input('Insira um novo valor: '))
        num2 = int(input('Insira outro valor: '))
    else:
        print('Escolha uma opção válida')