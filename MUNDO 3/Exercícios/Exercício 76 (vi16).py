lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Trasferidor', 4.2,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('-' * 50)
print('{: ^50}'.format('LISTAGEM DE PREÇOS'))
print('-' * 50)
for item in lista:
    print(f'{item:.<40}' if type(item) is str else '', end='')
    print(f'R${item: >7.2f}\n' if type(item) is float or type(item) is int else '', end='')
print('-' * 50)
