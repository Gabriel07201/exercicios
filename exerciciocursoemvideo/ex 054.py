from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(1,8):
    i = int(input(f'Em que ano a {c}° pessoa nasceu?'))
    a = ano - i
    if a < 18:
        menor += 1
    if a >= 18:
        maior += 1
print(f'Ao todo tivemos {menor} pessoas menores de idade')
print(f'E também tivemos {maior} pessoas maiores de idade')