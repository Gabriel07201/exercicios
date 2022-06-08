maiorp = menorp = 0
maiores = list()
menores = list()
pessoas = list()
grupo = list()
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maiorp = menorp = pessoas[1]
    else:
        if pessoas[1] > maiorp:
            maiorp = pessoas[1]
        if pessoas[1] < menorp:
            menorp = pessoas[1]
    grupo.append(pessoas[:])
    pessoas.clear()
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print(f'Ao todo você cadastrou {len(grupo)} pessoas.')
print(f'O o maior peso foi de {maiorp}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == maiorp:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menorp}Kg. Peso de ', end='')
for p in grupo:
    if p[1] == menorp:
        print(f'[{p[0]}] ', end='')
