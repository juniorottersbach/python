from math import hypot
# faça um programa que leia o cateto oposto e adjascente de um trangulo e mostra sua hipotenusa
opo = float(input("Informe a medida do cateto oposto: "))
adj = float(input("Informe a medida do cateto adjascente: "))
print("Com as medidas {} e {}, a hipotesua equivale a: {:.2f}".format(opo, adj, hypot(opo,adj)))