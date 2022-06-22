numeros = ((int(input('Digite um valor: '))), (int(input('Digite um valor: '))), (int(input('Digite um valor: '))),
           (int(input('Digite um valor: '))))
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu nenhuma vez')
pares = 0
for c in range(0,4):
    if numeros[c] % 2 == 0:
        pares += 1
print(f'Foram digitados {pares} valores pares')
