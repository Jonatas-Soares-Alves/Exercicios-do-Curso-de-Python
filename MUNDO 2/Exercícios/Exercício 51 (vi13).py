a1 = int(input('\nDigite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))

print('Aqui estão os 10 primeitos termos da sua PA: ')
print('\na1 = {}\nr = {}'.format(a1, r))

for pa in range(a1, a1+(r * 10), r):
    print('{}, '.format(pa),end='')

