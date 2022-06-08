exp = str(input('Digite uma expressão: ')).strip()
if exp.count('(') == exp.count(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')
