total = maiormil = pmaisbarato = 0
nome = ''
print('-'*40)
print('Loja'.center(40))
print('-'*40)
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cond = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    total += preço
    if pmaisbarato == 0:
        pmaisbarato += preço
        nome = produto
    elif pmaisbarato > preço:
        pmaisbarato += preço
        nome = produto
    if preço >= 1000:
        maiormil += 1
    if cond == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maiormil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${pmaisbarato:.2f}')
