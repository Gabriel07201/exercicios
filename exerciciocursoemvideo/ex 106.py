from time import sleep
while True:
    try:
        print('\033[1;42m~'*20)
        print('\033[1;42mSISTEMA DE AJUDA'.center(20))
        print('\033[1;42m~'*20)
        function = str(input('\033[mFunção da Biblioteca > '))
        def ajuda(function):
            print('\033[1;44m~'*20)
            print(f'Acessando o manual do comando {function}')
            print('\033[1;44m~'*20)
            help(function)
        ajuda(function)
        if function == 'FIM':
            break
    except:
        print('Comando inválido, tente novamente!')
