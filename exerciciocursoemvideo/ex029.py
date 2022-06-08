# um programa que leia a velocidade de um carro e se ele ultrapassar 80km/h, mostre uma mensagem de multado.
# a multa vai custar R$7 por cada Km acima do limite.
vel = float(input("Qual é a velocidade atual do carro?"))
multa = (vel - 80) * 7
if vel <= 80:
    print('Tenha um bom dia!Dirija com segurança!')
else:
    print(f'MULTADO! Você excedeu o limite de velocidade permitido que é de 80Km/h\nVocê deve pagar uma multa de '
          f'R${multa}!')
