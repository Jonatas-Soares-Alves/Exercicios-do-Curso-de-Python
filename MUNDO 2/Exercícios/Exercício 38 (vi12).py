n1 = float(input('\nDigite o 1º número: '))
n2 = float(input('\nDigite o 2º Número: '))

if n1 > n2:
    print('O \033[33m1º\033[m valor é maior! \033[33m({:.2f} > {:.2f})\033[m'.format(n1, n2))
elif n2 > n1:
    print('O \033[33m2º\033[m valor é maior! \033[33m({:.2f} > {:.2f})\033[m'.format(n2, n1))
else:
    print('\033[31mNão existe maior. \033[33mOs números {:.2f} e {:.2f} são iguaís!\033[m'.format(n1, n2))
