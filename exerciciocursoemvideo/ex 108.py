from modulos import ex108

p = float(input('Digite o preço: R$'))
print(f'A metade de {ex108.moeda(p)} é {ex108.moeda(ex108.metade(p))}')
print(f'O dobro de {ex108.moeda(p)} é {ex108.moeda(ex108.dobro(p))}')
print(f'Aumentando 10%, temos {ex108.moeda(ex108.aumentar(p))}')
