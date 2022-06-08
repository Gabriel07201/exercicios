homens = maior18 = mulher20 = 0
while True:
    print('-'*20)
    print('Cadastre uma pessoa'.upper())
    print('-'*20)
    i = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    if i > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if i < 20 and sexo == 'F':
        mulher20 += 1
    print('-'*20)
    cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos.')