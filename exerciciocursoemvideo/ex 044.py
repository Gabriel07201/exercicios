print('=' * 10, 'LOJA', '=' * 10)
p = float(input('Preço das compras: R$'))
print('FORMA DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
metodo = int(input('Qual é a opção? '))
if metodo == 1:
    print(f'Sua compra de R${p} vai custar {p-(p*0.10):.2f}')
if metodo == 2:
    print(f'Sua compra de R${p} vai custar {p-(p*0.05):.2f}')
if metodo == 3:
    print(f'Sua compra de R${p} vai custar 2 parcelas de R${p / 2:.2f}')
if metodo == 4:
    q = int(input('Quantidade de parcelas: '))
    print(f'Sua compra parcelada em {q}x de R${(p+(p*0.20))/q:.2f} COM JUROS')
    print(f'Sua compra de R${p} vai custar R${p+(p*0.20):.2f} no final.')
else:
    total = 0
    print('\033[1;31mOPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente!')