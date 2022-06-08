# calcular o aumento do salário. Para salários maiores que 1250 aumento de 10% para menores 15%
sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    print(f'Quem ganhava R${sal:.2f} passa a ganhar R${sal +(sal * 0.15):.2f} agora.')
else:
    print(f'Quem ganha R${sal:.2f} passa a ganhar R${sal + (sal * 0.10):.2f} agora.')
