def moeda(preco=0.0, cedula='R$'):
    return f'{cedula}{preco:.2f}'.replace('.', ',')


def metade(d=0, v=False):
    d = d / 2
    return d if v is False else moeda(d)


def dobro(d=0, v=False):
    d = d*2
    return d if v is False else moeda(d)


def aumentar(d=0, a=0, v=False):
    d = d * ((100 + a)/100)
    return d if v is False else moeda(d)


def diminuir(d=0, s=0, v=False):
    d = d * ((100 - s)/100)
    return d if v is False else moeda(d)


def resumo(d=0, aum=0, red=0):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'{"Preço analizado:":<25}{moeda(d)}')
    print(f'{"Dobro do preço:":<25}{dobro(d, True)}')
    print(f'{"Metade do preço:":<25}{metade(d, True)}')
    print(f'{f"{aum}% de aumento:":<25}{aumentar(d, aum, True)}')
    print(f'{f"{red}% de redução:":<25}{aumentar(d, red, True)}')
    print('-'*40)
