tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
# maneira mais resumida de se fazer a mesma coisa
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('--FIM--')

nome = str(input('Qual é seu nome?')).title().strip()
if nome == 'Gabriel':
    print('Que nome lindo você tem!')
else:
    print('Seu nome normal')
print(f'Bom dia, {nome}!')

n1 = float(input('Digite a prmeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 7.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')
print('PARABÉNS' if m >= 7.0 else 'ESTUDE MAIS')