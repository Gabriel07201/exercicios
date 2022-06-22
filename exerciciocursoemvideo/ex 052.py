n = int(input('Digite um número: '))
cont = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[32m',end='')
    else:
        print('\033[91m',end='')
    print(c,end=' ')
    if n % c == 0:
        cont += 1
print(f'\n\033[mO número {n} foi divisível {cont} vezes!')
if cont == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')