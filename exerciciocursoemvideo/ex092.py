from datetime import datetime
dicio = dict()
dicio['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dicio['idade'] = datetime.now().year - nascimento
dicio['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dicio['ctps'] != 0:
    dicio['contratação'] = int(input('Ano de contratação: '))
    dicio['salário'] = float(input('Salário: R$'))
    dicio['aposentadoria'] = dicio['idade'] + (dicio['contratação'] + 35) - datetime.now().year
for k, v in dicio.items():
    print(f'- {k} tem o valor {v}')
