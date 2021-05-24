from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0

for l in range(0, 7):
    nasc = int(input('\033[33m\nDigite o {}º ano de nascimento: \033[m'.format(l + 1)))
    if atual - nasc >= 21:
        cont1 += 1
        print('\033[32m\nA {}º pessoa JÁ É maior de idade\033[m'.format(l + 1))
    else:
        cont2 += 1
        print('\033[31m\nA {}º pessoa AINDA NÃO é maior de idade\033[m'.format(l + 1))

print('\n\033[1;33m{}\033[0;35m Pessoas são maior de idade! E \033[1;33m{}\033[0;35m ainda não!'.format(cont1, cont2))