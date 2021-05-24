#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#[[], [], []]
matriz = [[], [], []]
c1 = c2 = pares = 0
for e in range(0, 9):
    matriz[c1].append(int(input(f'Digite um valor para [{c1}, {c2}]: ')))
    if matriz[c1][c2] % 2 == 0:
        pares += matriz[c1][c2]
    c2 += 1
    if c2 == 3:
        c2 = 0
        c1 += 1
c1 = c2 = 0

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
