num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.insert(2, 0)
print(num)
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)
print(num)
if 4 in num: # se não fizer assim ele dá erro
    num.remove(4)
print(num)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

a = [2, 3, 4, 7]
b = a
print(a)
print(b)

a = [2, 3, 4, 7]
b = a # aqui ele acaba fazendo um ligação
b[2] = 8
print(a)
print(b)

a = [2, 3, 4, 7]
b = a[:] # aqui ele faz uma cópia
b[2] = 8
print(a)
print(b)