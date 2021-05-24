def ficha(nome='', gols=''):
    if len(nome) == 0:
        nome = '<desconheciodo>'
    if len(gols) == 0 or gols.isnumeric() is False:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de Gols: '))
ficha(n, g)
