# sem importaçao
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjascente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hipotesuna vai medir: {:.2f}".format(hi))