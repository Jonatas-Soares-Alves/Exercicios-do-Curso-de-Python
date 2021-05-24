from time import sleep


def contagem(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim}, pulando de {passo} em {passo}:')
    if inicio > fim:
        fim -= 1
    else:
        fim += 1
    if passo == 0:
        passo = 1
    elif inicio > fim and passo > 0:
        passo *= -1
    for n in range(inicio, fim, passo):
        print(f'{n} ', end='')
        sleep(0.5)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, -2)

print('\nAgora é sua vez! Digite os valores da sua contagem:\n')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))

contagem(inicio, fim, passo)
