def mensagem(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    print(f'A soma A + B = {a+b}\n')


def contador(*num):
    print(f'Recebi os valores {num} e são ao todo {len(num)} números')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


mensagem('Olá!')
mensagem('Esse é um teste')
mensagem('Vamos ver como isso funciona')

soma(3, 2)
soma(a=5, b=7)
soma(b=10, a=4)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

valores = [6, 3, 9, 1, 0, 2]
print('\n', valores)
dobra(valores)
print('\n', valores)

esc = 'O ponto tem de . estar em alguma parte'
print(esc)
esc = esc.replace('.', ',')
print(esc)

help(list.insert)
