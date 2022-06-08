dic = {}
dic['nome'] = str(input('Nome: '))
dic['média'] = float(input(f'Média de {dic["nome"]}: '))
print('-='*20)
if dic['média'] >= 7:
    dic['situação'] = 'Aprovado'
elif 5 <= dic['média'] <7:
    dic['situação'] = 'Recuperação'
else:
    dic['situação'] = 'Reprovado'
for k, v in dic.items():
    print(f'- {k} é igual a {v}')