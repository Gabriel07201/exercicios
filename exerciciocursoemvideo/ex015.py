print('Escreva um programa que pergunte a quantidade de Km percorridas por um carro alugado e a quantidade de dias'
      'pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por'
      'Km rodado.')
dias = int(input('Quantos dias alugados?'))
Km = float(input('Quantos Km rodados?'))
sd = dias * 60  # soma do valor em dias
sKm = Km * 0.15  # soma dos Km
t = sd + sKm
print(f'O total a pagar pelo aluguel é de R${t:.2f}')
