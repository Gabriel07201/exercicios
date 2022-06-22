d = str(input('Informe o seu sexo [M/F]:')).strip().upper()
while d not in 'MF':
    d = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo {d} registrado com sucesso')