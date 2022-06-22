posmaior = []
posmenor = []
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-'*20)
print(f'Você digitou os valores {valores}')
for c, v in enumerate(valores):
    if v == max(valores):
        posmaior.append(c)
    if v == min(valores):
        posmenor.append(c)
print(f'O maior valor digitado foi {max(valores)} nas posições {posmaior}')
print(f'O menor valor digitado foi {min(valores)} nas posições {posmenor}')
