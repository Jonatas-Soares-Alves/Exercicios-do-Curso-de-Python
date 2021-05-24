from time import sleep
def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    m = 0
    for i, n in enumerate(num):
        if i == 0:
            m = n
        elif n > m:
            m = n
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
