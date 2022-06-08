lista = [[], [], []]
cont = 0
while True:
    nome = str(input('Nome: '))
    lista[0].append(nome)
    nota1 = float(input('Nota 1: '))
    lista[1].append(nota1)
    nota2 = float(input('Nota 2: '))
    lista[2].append(nota2)
    cont += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar in 'N':
        break
print('-='*30)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*30)
for c in range(0,cont):
    print(f'{c:<4}{lista[0][c]:<10}{(lista[1][c] + lista[2][c]) / 2:>8}')
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    else:
        print(f'Notas de {lista[0][mostrar]} são [{lista[1][mostrar]}, {lista[2][mostrar]}]')
