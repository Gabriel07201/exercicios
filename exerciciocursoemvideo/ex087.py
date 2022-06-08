matriz = [[], [], []]
soma = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}] ', end='')
        valores = matriz[l][c]
        if valores % 2 == 0:
            soma += valores
        if c == 2:
            valores = matriz[l][c]
            terceira += valores
        if l == 1:
            valores = matriz[l][c]
            if maior == 0:
                maior = valores
            else:
                if valores > maior:
                    maior = valores
    print()
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')
