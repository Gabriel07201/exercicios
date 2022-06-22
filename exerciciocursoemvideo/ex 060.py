import math
acumulador = 1
n = int(input('Digite um número para calcular o seu fatorial: '))
print(f'O fatorial de {n} é {math.factorial(n)}')    #modo mais simples e rápido, tem como fazer com while e com for
for n in range(n,0,-1):
    acumulador *= n
print(acumulador)