from random import randint
from time import sleep


def sorteia():
    lista = []
    lista.clear()
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        num = randint(0, 9)
        print(f'{num} ', end='')
        lista.append(num)
        sleep(0.5)
    print('PRONTO!')
    return lista


def somaPar(lst):
    s = 0
    for n in lst:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {lst}, temos {s}')

somaPar(sorteia())
