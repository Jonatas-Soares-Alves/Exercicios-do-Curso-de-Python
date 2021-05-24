def contador(i, f, p):
    """
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Função criada por: Jônatas Soares Alves - 24/02/2021
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
        print('FIM!')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


help(contador)

print(somar(2, 3, 4))
print(somar(3, 2))
print(somar(2))
print(somar(b=2, a=1))

num = 4
if par(num):
    print('\nÉ par!')
else:
    print('\nNão é par!')
