lst =[]
maior = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}° pessoa:'))
    lst += [peso]
print('O maior peso foi',max(lst),'Kg')
print('O menor peso foi', min(lst),'Kg')