print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)
dinheiro = float(input('Quanto quer sacar? R$'))
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while True:
    if dinheiro >= 50:
        n50 += 1
        dinheiro -= 50

    elif 50 > dinheiro >= 20:
        n20 += 1
        dinheiro -= 20

    elif 20 > dinheiro >= 10:
        n10 += 1
        dinheiro -= 10

    elif 10 > dinheiro >= 1:
        n1 += 1
        dinheiro -= 1

    else:
        break

if n50 > 0:
    print(f'Total de {n50} cédulas de R$50')
if n20 > 0:
    print(f'Total de {n20} cédulas de R$20')
if n10 > 0:
    print(f'Total de {n10} cédulas de R$10')
if n1 > 0:
    print(f'Total de {n1} cédulas de R$1')
print('=' * 40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
