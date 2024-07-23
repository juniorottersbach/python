print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²')
v1 = float(input('Informe a largura da parede: '))
v2 = float(input('Informe a altura da parede: '))
print('Área da parede: {}m²\nQuantidade de tinta necessária: {}L'.format(v1*v2,(v1*v2)/2))