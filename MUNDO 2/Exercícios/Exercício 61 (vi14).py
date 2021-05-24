a1 = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))

pa = 0
r1 = 0

print('\nOs 10 primeiros termos da sua PA são:')

while pa != a1 + (9 * r):
    pa = a1 + r1
    r1 += + r
    print('{}, '.format(pa), end='')
