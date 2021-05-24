def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-'*40)
    f = 1
    for c in range(n, 0, -1):
        if show is True:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    print(f)
    return f


fatorial(5, show=False)
help(fatorial)
