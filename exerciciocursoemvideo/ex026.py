# um programa que leia uma frase e mostre: quantas vezes aparece a letra "a"; em que posição ela aparece a primeira vez
# em que posição ela aparece pela última vez
frase = str(input('Digite uma frase:')).strip()
print(f'A letra A aparece {frase.lower().count("a")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.lower().find("a")+1}')
print(f'A última letra A apareceu na posição {frase.lower().rfind("a")+1}')
