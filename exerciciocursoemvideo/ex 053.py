frase = str(input('Digite uma frase: '))
palavras = frase.split()
junto = ''.join(palavras)
frasi = junto[::-1]
print(f'O inverso de {junto} é {frasi}')
if junto == frasi:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')