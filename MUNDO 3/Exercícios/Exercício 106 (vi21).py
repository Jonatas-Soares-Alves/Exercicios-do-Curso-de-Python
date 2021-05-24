def pyhelp():
    while True:
        print('\033[1:42m' + '~' * 27)
        print('  SISTEMA DE AJUDA PyHELP')
        print('~' * 27)
        func = str(input('\033[mFunção ou Biblioteca > '))
        if 'FIM' in func.upper():
            print('\033[1:41m' + '~'*13)
            print('  ATÉ LOGO!')
            print('~'*13)
            break
        txt = 'Acessando o manual do comando ' + func
        print('\033[1:44m' + '~'*(len(txt) + 4))
        print(f'  {txt}')
        print('~'*(len(txt) + 4))
        print('\033[m\033[7m', end='')
        print(help(func))
        print('\033[m')


pyhelp()
