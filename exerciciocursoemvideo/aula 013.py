for c in range(1, 6):
    print('Oi')
print('FIM')
for c in range(0, 6):
    print('Olá')
print('FIM')
for c in range(1, 6):
    print(c)
print('FIM')
for c in range(6, 0, -1): #para contar regressivamente
    print(c)
print('FIM')
for c in range(0, 8, 2):
    print(c)
print('FIM')
n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)
print('FIM')
for c in range(0, n+1):
    print(c)
print('FIM')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
for c in range(0, 3):
    n = int(input('Digite um valor: '))
print('FIM')
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s = s + n
print(f'O somatório de todos os valores foi {s}')