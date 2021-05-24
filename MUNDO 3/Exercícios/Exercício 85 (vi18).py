lista = [[], []]
for v in range(0, 6):
    n = int(input(f'Digite o {v+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(f'''
Os valores PARES digitados foram: {lista[0]}
Os valores ÍMPARES digirados foram: {lista[1]}
''')
