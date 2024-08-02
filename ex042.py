a = float(input('Informe a reta 1: '))
b = float(input('Informe a reta 2: '))
c = float(input('Informe a reta 3: '))
if (b - c) < a < b + c or (a - c) < b < a + c or (a - b) < c < a + b:
    print('Essas retas podem formar um triângulo')
    if a == b and b == c:
        print('E elas formam um triângulo equilátero')
    elif a == b or b == c or a == c:
        print('E elas formam um triângulo isóceles')
    else:
        print('E elas formam um triângulo escaleno')
else:
    print('Essas retas não podem formar um triângulo')