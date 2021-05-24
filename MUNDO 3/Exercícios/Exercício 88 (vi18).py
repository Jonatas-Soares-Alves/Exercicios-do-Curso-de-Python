from time import sleep
from random import randint
jogadas = []
jog = []
print('-'*45)
print(f'{"JOGA NA MEGA SENA":^45}')
print('-'*45)

qnt = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f" SORTEANDO {qnt} JOGOS ":=^45}')
for n in range(0, qnt):
    cont = 0
    while True:
        tent = randint(1, 60)
        if tent not in jog:
            jog.append(tent)
            cont += 1
        if cont == 6:
            break

    jogadas.append(sorted(jog[:]))
    jog.clear()
    print(f'Jogo {n+1}: {jogadas[n]}')
    sleep(0.5)
print(f'{f"< BOA SORTE! >":=^45}')

