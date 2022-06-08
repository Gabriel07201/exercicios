valores = [[], []]
for n in range(0, 7):
    numeros = int(input(f'Digite o {n+1}° valor: '))
    if numeros % 2 == 0:
        valores[0].append(numeros)
    else:
        valores[1].append(numeros)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
