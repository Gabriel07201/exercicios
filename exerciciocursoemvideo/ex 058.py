from random import randint
n = randint(0,10)
c = 1
j = int(input('Acabei de pensar em um número entre 0 e 10, consegue acertar qual foi?'))
while j != n:
    if j < n:
        j = int(input('Mais...Tente mais uma vez: '))
        c += 1
    else:
        j = int(input('Menos...Tente mais uma vez: '))
        c += 1
print(f'Acertou com {c} tentativas.')