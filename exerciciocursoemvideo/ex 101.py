def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    print(f'Com {idade} anos:', end=' ')
    if idade < 16:
        print('NÃO VOTA')
    elif 16 <= idade < 18 or idade > 70:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATÓRIO')


nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)
print('teste')
