print('='*30)
print('10 TERMOS DE UM PA'.center(30))
print('='*30)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = n + (10 - 1) * r
for c in range(n,décimo,r):
    print(c,end=' → ')
print('ACABOU')