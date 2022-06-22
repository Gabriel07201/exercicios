print('\033[1;31;43mOlá, mundo!')
print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;97;45mOlá, mundo!\033[m')
print('\033[97mOlá, mundo!\033[m')
print('\033[7;97mOlá, mundo!\033[m')
print('\033[0;33;44mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}')
limpa = '\033[m'
azul = '\033[34m'
amarelo = '\033[33m'
pretoebranco = '\033[7;97m'
verde = '\033[32m'
vermelho = '\033[31m'
print(f'{limpa}Os valores são {verde}{a}{limpa} e {vermelho}{b}{limpa}')
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')
print(f'{verde}Olá,{limpa}{azul}mundo!!{limpa}')
