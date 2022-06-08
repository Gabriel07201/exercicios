tupla = ('aprender', 'programar', 'linguagem')
for c in tupla:
    print('\nNa palavra 'f'{c.upper()} temos ', end='')
    for letra in c:
        if letra in 'aeiou':
            print(letra, end=' ')