def leiaInt():
    while True:
        n = (input('Digite um número: '))
        if n.isnumeric() == False:
            print('	\033[1;31mERRO! Digite um número válido.\033[m')
        if n.isnumeric():
            break
    return n


leiaInt()
print(f'Você acabou de digitar o número {n}')
