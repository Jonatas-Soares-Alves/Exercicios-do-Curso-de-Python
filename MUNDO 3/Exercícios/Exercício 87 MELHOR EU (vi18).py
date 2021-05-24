matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

print(f'''
|-----|-----|-----|
|{matriz[0][0]:^5}|{matriz[0][1]:^5}|{matriz[0][2]:^5}|
|-----|-----|-----|
|{matriz[1][0]:^5}|{matriz[1][1]:^5}|{matriz[1][2]:^5}|
|-----|-----|-----|
|{matriz[2][0]:^5}|{matriz[2][1]:^5}|{matriz[2][2]:^5}|
|-----|-----|-----|
''')

print(f'''A soma dos valores pares é {pares}.
A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.
O maior valor da segunda linha é {max(matriz[1])}.
''')
