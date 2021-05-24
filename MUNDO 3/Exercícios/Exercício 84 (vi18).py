pessoas = []
dados = []
pesados = []
leves = []
pesos = []
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    pesos.append(dados[1])
    dados.clear()

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break

for d in pessoas:
    if d[1] == max(pesos):
        pesados.append(d[0])
    elif d[1] == min(pesos):
        leves.append(d[0])

print(f'''
ANALISE DOS DADOS:
{len(pessoas)} Pessoas cadastradas.
O MAIOR peso foi de {max(pesos):.1f}Kg. Peso de {pesados}.
O menor peso foi de {min(pesos):.1f}Kg. Peso de {leves}
''')
