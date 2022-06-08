print('Simulador de caixa eletrônico.')
saque = sacar = 0
while saque != 1:
    sacar = float(input('Qual valor você quer sacar? R$'))
    nota50 = sacar // 50
    nota20 = (sacar % 50) // 20
    nota10 = ((sacar % 50) % 20) // 10
    nota1 = (((sacar % 50) % 20) % 10) // 1
    saque += 1
if nota50 > 0:
    print(f'Total de {nota50:.0f} cédulas de R$50.00')
if nota20 > 0:
    print(f'Total de {nota20:.0f} cédulas de R$20.00')
if nota10 > 0:
    print(f'Total de {nota10:.0f} cédulas de R$10.00')
if nota1 > 0:
    print(f'Total de {nota1:.0f} cédulas de R$1.00')
