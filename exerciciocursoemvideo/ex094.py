lista = []
dicio = {}
media = 0
mulheres = []
acima = []
while True:
    dicio['nome'] = str(input('Nome: '))
    dicio['sexo'] = str(input('Sexo: [M/F]')).strip().upper()
    while dicio['sexo'] not in 'MF':
        del dicio['sexo']
        print('Por favor, digite apenas M ou F.')
        dicio['sexo'] = str(input('Sexo: [M/F]')).strip().upper()
    dicio['idade'] = int(input('Idade: '))
    media += dicio['idade']
    lista.append(dicio.copy())
    if dicio['sexo'] in 'F':
        mulheres.append(dicio.copy())
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar in 'N':
        break
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'A média de idade é de {media / len(lista)} anos.')
for c, x in enumerate(mulheres):
    if c == 0:
        print(f'As mulheres cadastradas foram {mulheres[c]["nome"]}', end=' - ')
    else:
        print(f'{mulheres[c]["nome"]}', end=' - ')
media = media / len(lista)
print('\nLista das pessoas que estão acima da média:')
for a, b in enumerate(lista):
    if lista[a]['idade'] > media:
        print(f'   nome = {lista[a]["nome"]}; sexo = {lista[a]["sexo"]}; idade = {lista[a]["idade"]}')
