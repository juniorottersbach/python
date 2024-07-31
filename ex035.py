a = float(input('Informe a reta 1: '))
b = float(input('Informe a reta 2: '))
c = float(input('Informe a reta 3: '))
if (b - c) < a < b + c or (a - c) < b < a + c or (a - b) < c < a + b:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')