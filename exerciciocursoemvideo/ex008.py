print('Escreva um programa que leia um valor em metros e o exiba convertido em centrímetros e milímetros')
n = float(input('Digite um valor em metros:'))
c = n * 100
m = c * 10  # milímetros
print(f'Metros:{n}\nCentímetros:{c}\nMilímetros:{m}')
dc = n/10
km = n/1000
print(f'Km:{km}\nDecametro:{dc}')
