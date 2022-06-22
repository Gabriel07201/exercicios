lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
for comida in lanche:
    print(f'{comida}')
print(len(lanche))
for cont in range(0, len(lanche)):
    print(cont)
for cont in range(0, len(lanche)):
    print(lanche[cont])
for pos, comida in enumerate(lanche):
    print(f'Comida {comida} posição {pos}')
print(sorted(lanche)) #ordenado em ordem

a = (2, 5, 4)
b = (5, 8,1, 2)
print(a)
print(b)
c = a + b
print(c)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.count(4))
print(c.index(8)) # mostra a posição
print(c.index(5)) #mostra a primeira ocorrencia
print(c.index(5, 1)) #para ver a partir de outra posição
pessoa = ('Gustavo', 39, 'M', 99.88)
del pessoa
print(pessoa)
