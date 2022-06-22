n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo Valor: '))
op = 0
resp = '\033[32m'
semcor = '\033[m'
while op != 5:
    print('=-' * 15)
    print('''[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa''')
    op = int(input('Qual sua opção?'))
    if op == 1:
        print(f'{resp}A soma entre {n1} + {n2} é {n1+n2}{semcor}')
    if op == 2:
        print(f'{resp}A multiplicação entre {n1} x {n2} é {n1*n2}{semcor}')
    if op == 3:
        if n1 > n2:
            print(f'{resp}O maior número é {n1}{semcor}')
        if n1 < n2:
            print(f'{resp}O maior número é {n2}{semcor}')
        else:
            print(f'{resp}Os dois são iguais{semcor}')
    if op == 4:
        print('Informes os números novamente.')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo Valor: '))
    if op < 1 or op > 5:
        print('Opção inválida, tente novamente.')
        op = int(input('Qual sua opção?'))
    if op == 5:
        print('Fim do programa')
