lista = list()
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'\nLista: {lista}')
print(f'\nO maior valor digitado foi: {max(lista)} na posição: ', end='')
for pos, num in enumerate(lista):
    if num == max(lista):
        print(f'{pos+1} ', end='')
print(f'\nO menor valor digitado foi: {min(lista)} na posição: ', end='')
for pos, num in enumerate(lista):
    if num == min(lista):
        print(f'{pos+1} ', end='')
