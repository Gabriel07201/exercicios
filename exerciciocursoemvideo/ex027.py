# um programa que leia o nome completo de uma pessoa e mostre depois o seu primeiro e último nome
nome = str(input('Qual seu nome completo?')).title() .strip()
lista = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {lista[0]}')
print(f'Seu último nome é {lista[-1]}')
