while True:
    print('-'*40)
    t = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*40)
    if t < 0:
        break
    for c in range(1,11):
        print(f'{t} x {c:2} = {t*c}')
print('PROGRAMA ENCERRADO. Volte sempre.')
