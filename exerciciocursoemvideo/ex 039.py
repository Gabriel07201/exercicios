from datetime import date
atual = date.today().year
data = int(input('Ano de nascimento:'))
alistamento = atual - data
print(f'Quem nasceu em {data} tem {alistamento} anos em {atual}')
if alistamento == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif alistamento < 18:
    saldo = 18 - alistamento
    print(f'Ainda faltam {saldo} anos para o seu alistamento\nSeu alistamento será em {saldo+atual}')
else:
    saldo = alistamento - 18
    print(f'Você já deveria ter se alistado há {saldo} anos\nSeu alistamento foi em  {atual-saldo}')
