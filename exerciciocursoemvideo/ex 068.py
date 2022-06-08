import random
cont = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    j = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
        print('-'*40)
    c = random.randint(0,10)
    soma = j + c
    if soma % 2 == 0:
        print(f'Você jogou {j} e o computador {c}. Total de {soma} DEU PAR')
        print('-' * 40)
        if pi in 'Pp':
            print('Você VENCEU')
            print('Vamos jogar novamente...')
            print('=-'*20)
            cont += 1
        elif pi == 'Ii':
            print('Você PERDEU')
            break
    if soma % 2 != 0:
        print(f'Você jogou {j} e o computador {c}. Total de {soma} DEU ÍMPAR')
        print('-' * 40)
        if pi == 'Ii':
            print('Você VENCEU')
            print('Vamos jogar novamente...')
            print('=-'*20)
            cont += 1
        else:
            print('Você PERDEU')
            break
print(f'GAME OVER. Você venceu {cont} vezes.')