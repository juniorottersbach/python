from math import radians, sin, cos, tan
# faça um programa que leia um angulo qualquer e mostre o valor do seno cosseno e tangente
ang = float(input("Informe um ângulo qualquer: "))
print("O angulo de: {} possui os valores: \nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(ang, sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))