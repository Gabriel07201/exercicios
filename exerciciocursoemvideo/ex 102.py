def fatorial(n, show=''):
    """
    Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: o valor fatorial de um número n.
    """
    resultado = 1
    for c in range(n, 1, -1):
        resultado *= c
        if show:
            print(f'{c} x ', end='')
    if show:
        return print(f' = {resultado}')
    else:
        return print(resultado)


help(fatorial)
