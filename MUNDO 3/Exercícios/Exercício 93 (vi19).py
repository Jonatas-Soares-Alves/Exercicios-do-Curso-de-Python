jogador = dict()
gols = list()

jogador['nome'] = str(input('Nome do Jogador: ')).strip()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na {g+1}º partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('\n', jogador, '\n')

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.\n')

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
