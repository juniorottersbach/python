pre = float(input('Informe o preço do produto: R$'))
opc = int(input('Como deseja pagar?\n1 - para à vista no dinheiro/cheque\n2 - à vista no cartão\n3 - até 2 parcelas\n4 - 3 ou mais parcelas\n'))
if opc == 1:
    print('Valor originar: R${:.2f}\nValor ajustado: R${:.2f}'.format(pre, pre * 0.9))
elif opc == 2:
    print('Valor originar: R${:.2f}\nValor ajustado: R${:.2f}'.format(pre, pre * 0.95))
elif opc == 3:
    print('Valor originar: R${:.2f}\nValor ajustado: R${:.2f}'.format(pre, pre))
elif opc == 4:
    print('Valor originar: R${:.2f}\nValor ajustado: R${:.2f}'.format(pre, pre * 1.20))

else:
    print('Escolha uma opção válida.')