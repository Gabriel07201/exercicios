print('Um programa que leia um número inteiro e mostre o seu antecessor e o seu sucessor.')
n = int(input('Digite um número:'))
ant = n - 1
suc = n + 1
print(f'O seu número é {n}, seu antecessor é {ant} e o seu sucessor é {suc}')  # aqui eu poderia ter colocado a
# operação no lugar do ant e do suc, assim eu não criaria mais duas variáveis.
