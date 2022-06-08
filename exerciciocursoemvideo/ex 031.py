# calcular o custa da passagem de uma viajem que tem 2 variáveis de valor dependendo do Km
n = float(input('Qual a distância da viajem?'))
print(f'Você está prestes a começar uma viajem de {n}Km.')
if n <= 200:
    print(f'E o preço da sua passagem será de R${n * 0.5:.2f}')
else:
    print(f'E o preço da sua passagem será de R${n * 0.45:.2f}')
