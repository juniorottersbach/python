print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
p = float(input('Km percorridos: '))
q = float(input('Dias alugado: '))
print('Total a pagar: R${:.2f}'.format((q*60)+(p*0.15)))