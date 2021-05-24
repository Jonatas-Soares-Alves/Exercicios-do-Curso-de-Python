selecao = list()
jogador = dict()
gols = list()
cont = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for g in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na {g+1}º partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    selecao.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
    print('-'*40)

print(f'\n{"cod":<3} {"nome":<20} {"gols":<20} {"total":<5}')
print('-'*52)
for c in range(0, len(selecao)):
    print(f'{c:<3} {selecao[c]["nome"]:<20} {str(selecao[c]["gols"]):<20} {selecao[c]["total"]:<5}')
print('-'*52)

while True:
    jog = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if jog == 999:
        break
    if jog > len(selecao)-1 or jog < 0:
        print(f'\033[31mERRO Não existe jogador com código {jog}! Tente novamente\033[m')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {selecao[jog]["nome"]}:')
        for i, v in enumerate(selecao[jog]['gols']):
            print(f'   No jogo {i+1} fez {v} gols.')
    print('-' * 52)

print('<< VOLTE SEMPRE >>')
