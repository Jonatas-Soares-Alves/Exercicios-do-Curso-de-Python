ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('\nDigite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'\nVocê digitou o número {ext[n]}.')
    else:
        print('\n\033[31mNúmero inválido!\033[m')

    while True:
        continuar = input('\nQuer continuar? [S/N]: ').strip().upper()[0]
        if continuar in 'SN':
            break

    if 'N' in continuar:
        break

print('FECHANDO PROGRAMA')
