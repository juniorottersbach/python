pv = int(input('Informe o primeiro valor: '))
ra = int(input('Informe a razão: '))
pv1 = pv
ra1 = ra
parada = 10
mais = 0
c = 0
m = 1
while m != 0:
    if c < parada:
        print(pv, end=' ')
        pv += ra
        c += 1
    elif c == parada:
        mais = int(input('\nQuer mostrar mais alguns termos? [0 para sair]: '))
        if mais == 0:
            m = 0
        else:
            parada += mais
            pv = pv1
            ra = ra1
            c = 0