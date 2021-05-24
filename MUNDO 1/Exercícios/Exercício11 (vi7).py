lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = lar * alt

print('A sua parede vai precisar de {:.2f} litros de tinta.'.format(area/2))
