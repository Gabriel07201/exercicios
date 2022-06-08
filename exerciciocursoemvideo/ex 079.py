lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    o = str(input('Gostaria de continuar? [S/N]')).upper().strip()
    if valor not in lista:
        lista.insert(0, valor)
    if o in 'N':
        break
lista.sort()
print('-='*20)
print(f'Você digitou os valores {lista}')
