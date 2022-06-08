soma = 0
cont = 0
somap = 0
contp = 0
for c in range(6):
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if n % 2 == 0:
        contp += 1
        somap += n
print(f'Você informou {cont} números e a soma foi {soma}, já a soma dos {contp} números pares foi {somap}')