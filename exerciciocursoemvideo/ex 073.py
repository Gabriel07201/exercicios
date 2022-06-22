times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético',
         'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Lista de times do Brasileirão: {times}')
print(f'Os cinco primeiros são: {times[:5]}')
print(f'Os últimos 4 são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O time da Chapecoense está em {times.index("Chapecoense")+1}° lugar')