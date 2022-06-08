print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')
p = float(input('Informe o preço do produto:R$'))
d = p * 0.05  # desconto
pf = p - d  # preço final
print(f'O preço com o desconto é:R${pf:.2f}')
