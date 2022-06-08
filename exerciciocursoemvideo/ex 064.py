c = 0
nc = -1
soma = -999
while c != 999:
    n = int(input('Digite um número [999 para parar]: '))
    c = n
    nc += 1
    soma += n
print(f'Você digitou {nc} números e a soma entre eles foi {soma}')