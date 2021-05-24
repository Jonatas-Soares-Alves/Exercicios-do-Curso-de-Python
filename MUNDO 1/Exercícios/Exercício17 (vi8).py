from math import hypot

op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))

h = hypot(ad, op)

print('A hipotenusa de {} e {} é {}'.format(op, ad, h))