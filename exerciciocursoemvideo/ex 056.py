media = 0
contf = 0
hmv = ''
ihmv = 0
for p in range(1, 5):
    print('-' * 8, f'{p}° pessoa', '-' * 8)
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade
    if sexo == 'F' and idade < 20:
        contf += 1
    if sexo == 'M' and p == 1:
        hmv = nome
        ihmv = idade
    if sexo == 'M' and idade > ihmv:
        hmv = nome
        ihmv = idade
media = media / p
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {ihmv} anos e se chama {hmv}')
print(f'Ao todo são {contf} mulheres com menos de 20 anos')
