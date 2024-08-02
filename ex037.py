num = int(input('Informe um número: '))
menu = int(input('Informe a conversão desejada:\n1 para binário\n2 octal\n3 para hexadecimal\n'))
if menu == 1:
    print('Valor binário: {}'.format(bin(num)[2:]))
elif menu == 2:
    print('Valor octal: {}'.format(oct(num)[2:]))
elif menu == 3:
    print('Valor hexadecimal: {}'.format(hex(num)[2:]))
else:
    print('Escolha uma opção valida.')