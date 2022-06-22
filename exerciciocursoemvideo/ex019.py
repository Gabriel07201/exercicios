import random
# sortear um aluno em uma lista de 4 alunos
a1 = str(input('Primeiro aluno:'))
a2 = str(input('Segundo aluno:'))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Qaurto aluno:'))
lista = [a1, a2, a3, a4]
print(f'O aluno escolhido foi {random.choice(lista)}')
