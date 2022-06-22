c = 1
n = int(input('Digite um número: '))
maior = n
menor = n
m = n
sn = str(input('Quer continuar? [S/N]')).upper()
while sn not in 'N':
    n = int(input('Digite um número: '))
    if n < menor:
        menor = n
    elif n > maior:
        maior = n
    c += 1
    m += n
    sn = str(input('Quer continuar? [S/N]')).upper().strip()
print(f'Você digitou {c} números e a média foi {m/c}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
