from random import randrange

usua = int(input('''
\033[1;35mO computador vai pensar em um número de 0 até 5.
Tente advinhas no número que o computador pensou: \033[m'''))

comp = randrange(6)

if usua == comp:
    print('\n\033[7;32mVocê VENCEU!\033[0;32m O computador pensou no número "{}" e você em "{}.\033[m"'.format(comp, usua))
else:
    print('\n\033[7;31mVocê PERDEU!\033[0;31m O computador pensou no número "{}" e você em "{}".\033[m'.format(comp, usua))

print('\n\033[7mFim de jogo!\033[m')
