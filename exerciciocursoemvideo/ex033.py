# ler 3 número e mostrar qual é o maior e qual o menor
n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
n3 = int(input('Terceiro valor:'))
if n1 < n2 < n3:
    print(f'O menor número é {n1}')
if n2 < n1 < n3:
    print(f'O menor número é {n2}')
if n3 < n1 < n2:
    print(f'O menor número é {n3}')
if n1 > n2 > n3:
    print(f'O maior número é {n1}')
if n2 > n1 > n3:
    print(f'O maior número é {n2}')
if n3 > n1 > n2:
    print(f'O maior número é {n3}')

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor número é {menor}')
if n1 < n2 and n1 < n3:
    maior = n1
if n2 < n1 and n2 < n3:
    maior = n2
if n3 < n1 and n3 < n2:
    maior = n3
print(f'O maior número é {maior}')
