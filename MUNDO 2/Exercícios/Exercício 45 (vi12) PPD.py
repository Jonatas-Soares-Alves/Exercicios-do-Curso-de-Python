from random import randrange
from time import sleep

jogador = int(input('''
\033[1:36mVamos jogar Jokenpô!\033[0:35m
[ 1 ] = Pedra!
[ 2 ] = Papel!
[ 3 ] = Tesoura!
'''))

comp = (randrange(3)+1)

print('\033[1:33mJO!\033[m')
sleep(1)
print('\033[1:33mKEN!\033[m')
sleep(1)
print('\033[1:33mPÔ!\033[m')
sleep(1)

#===============PEDRA==================
if jogador == 1 and comp == 1:
    print('''
    \033[36mVocê: PEDRA
    \033[35mComputador: PEDRA
    
    \033[1:33mEMPATE!\033[m
    ''')
elif jogador == 1 and comp == 2:
    print('''
    \033[36mVocê: PEDRA
    \033[35mComputador: PAPEL

    \033[1:31mPERDEU!\033[m
    ''')
elif jogador == 1 and comp == 3:
    print('''
    \033[36mVocê: PEDRA
    \033[35mComputador: TESOURA

    \033[1:32mVENCEU!\033[m
    ''')
#===============PEDRA==================

#===============PAPEL==================
elif jogador == 2 and comp == 1:
    print('''
    \033[36mVocê: PAPEL
    \033[35mComputador: PEDRA

    \033[1:32mVENCEU!\033[m
    ''')
elif jogador == 2 and comp == 2:
    print('''
    \033[36mVocê: PAPEL
    \033[35mComputador: PAPEL

    \033[1:33mEMPATE!\033[m
    ''')
elif jogador == 2 and comp == 3:
    print('''
    \033[36mVocê: PAPEL
    \033[35mComputador: TESOURA

    \033[1:31mPERDEU!\033[m
    ''')
#===============PAPEL==================

#===============TESOURA==================
elif jogador == 3 and comp == 1:
    print('''
    \033[36mVocê: TESOURA
    \033[35mComputador: PEDRA

    \033[1:31mPERDEU!\033[m
    ''')
elif jogador == 3 and comp == 2:
    print('''
    \033[36mVocê: TESOURA
    \033[35mComputador: PAPEL

    \033[1:32mVENCEU!\033[m
    ''')
elif jogador == 3 and comp == 3:
    print('''
    \033[36mVocê: TESOURA
    \033[35mComputador: TESOURA

    \033[1:33mEMPATE!\033[m
    ''')
#===============TESOURA==================

else:
    print('\033[7:31mJOGADA INVÁLIDA!!!\033[m')
