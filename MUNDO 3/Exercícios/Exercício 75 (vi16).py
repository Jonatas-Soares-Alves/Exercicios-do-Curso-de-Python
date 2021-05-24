tup = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
       int(input('Digite um valor: ')), int(input('Digite um valor: ')))

print(f'O valor 9 apareceu {tup.count(9)} vezes')

if tup.count(3) > 0:
    print(f'O primeiro 3 está na {tup.index(3) + 1}º posição.')
else:
    print('Não há valor 3 nessa tupla')

print('Os números pares são: ', end='')
for num in tup:
    print(f'{num} ' if num % 2 == 0 else '', end='')
