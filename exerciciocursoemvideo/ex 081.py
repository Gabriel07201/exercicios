lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    o = str(input('Quer continuar? [S/N]')).upper().strip()
    if o in 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort()
print(f'Os valores em ordem decrescente são {lista[::-1]}')
if 5 in lista:
    print('O valor 5 faz parte dessa lista!')
else:
    print('O valor 5 não faz parte dessa lista.')
