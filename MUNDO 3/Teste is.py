par = []
imp= []

text = 5
continuar = ''
lista = [5, 6, 7, 8]
print(type(text))

print(f'{text: >7.2f}' if type(text) is int else '')

print('SN' in continuar)

for pos, num in enumerate(lista):
    print(f'Posição {pos} e número {num}')

cont = 0
while True:
    if len(lista) == cont:
        break
    print(f'{lista[cont]}')
    cont += 1

for pos, n in enumerate(lista):
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)


print(f'''
Lista: {lista}
Pares: {par}
Impares: {imp}
''')

num = [2, 8, 4, 7]
num.pop()
num.insert(1, 3)
num.append(6)
print(num)
