valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = float(input('Quantos anos de financiamento? '))
prestacao = valor/(anos*12)
print(f'Para pagar uma casa de R${valor} em {anos} anos a prestação será de R${prestacao:.2f}')
emprestimo = salario*0.3
if prestacao > emprestimo:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
