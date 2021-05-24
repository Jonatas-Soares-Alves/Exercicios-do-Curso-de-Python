dist = int(input('''
Preços:
Viagem abaixo de 200km = R$0.50/km
Viagem acima de 200km = R$0.45/km
Digite a distância em Km da viagem: '''))

if dist <= 200:
    cust = float (dist * 0.5)
else:
    cust = float (dist * 0.45)
print('\nA viágem custará R${:.2f}'.format(cust))
