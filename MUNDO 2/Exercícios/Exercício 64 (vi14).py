cont1 = 0
cont2 = 0
r = int(input('\nDigite um valor inteiro: '))
while r != 999:
    cont1 += +1
    cont2 += r
    r = int(input('\nDigite um valor inteiro: '))
print('Você digitou {} números e a soma deles é {}'.format(cont1, cont2))
