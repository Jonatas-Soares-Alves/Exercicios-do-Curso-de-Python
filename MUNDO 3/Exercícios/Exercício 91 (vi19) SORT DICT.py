from random import randint
from time import sleep
from operator import itemgetter
jogadas = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6),}
ranking = list()
for k, v in jogadas.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DOS JOGADORES ==')

for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar {v[0]} com {v[1]}')
    sleep(0.5)
