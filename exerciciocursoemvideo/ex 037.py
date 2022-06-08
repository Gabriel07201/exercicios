n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases abaixo para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print(f'{n} convertido para BINÁRIO é igual à {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para OCTAL é igual à {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para HEXADECIMAL é igual à {hex(n)[2:]}')
else:
    print('Opção selecionada inválida!!')
