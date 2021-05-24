lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
    else:
        for pos, num in enumerate(lista):
            print(f'Posição {pos} e número {num}')
            if num >= n:
                lista.insert(n, pos)
            else:
                lista.append(n)
                break
            print(f'{n} colocado na posição {pos}')

print(lista)
