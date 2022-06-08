print('10 Termos de uma PA')
print('-='*10)
p1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cálculo = 0
limite = 10
pa = 0
while cálculo < limite:
    if pa == 0:
        pa += p1
        cálculo += 1
    else:
        pa += r
        cálculo += 1
    print(pa, end=' → ')
print('PAUSA')
c = 1
nlimite = limite
while c != 0:
    c = int(input('Quantos termos você quer mostrar a mais?'))
    nlimite += c
    while cálculo < nlimite:
        pa += r
        cálculo += 1
        print(pa, end=' → ')
    print('PAUSA')
    if c == 0:
        print(f'Progressão finalizada com {cálculo} termos mostrados.')