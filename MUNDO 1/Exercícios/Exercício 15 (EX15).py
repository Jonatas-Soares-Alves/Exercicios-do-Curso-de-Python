d = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos quilometros foram rodados? '))

pre = (d * 60) + (km * 0.15)

print('Você deverá pagar: R${:.2f}'.format(pre))
