a1 = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))

mais = 1
pa = 0
r1 = 0
termo = 9

while mais != 0:
    print('\nOs {} termos da sua PA são: '.format(termo + 1))

    while pa != a1 + (termo * r):
        pa = a1 + r1
        r1 += + r
        print('{}, '.format(pa), end='')

    mais = int(input('\n\nQuer ver mais quantos termos? '))
    termo += mais

print('\nFechando programa!')