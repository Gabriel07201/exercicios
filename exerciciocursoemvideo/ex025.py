# Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome
nome = str.title(input('Qual seu nome completo?')).strip()
print('Silva' in nome)
