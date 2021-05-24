from time import sleep

idadeh = 0
media = 0
contm = 0
nomeh=''

for l in range(1, 5):

    l = str(l)

    print('---------- {}º PESSOA ----------'.format(l))
    nome = input('Nome? ').strip()
    idade = int(input('Idade? ').strip())
    sexo = input('Sexo? [H/M]? ').strip().upper()

    if sexo in 'Hh' or sexo in 'Mm':
        media += idade

        if idade > idadeh and sexo in 'Hh':
            idadeh = idade
            nomeh = nome
        elif idade < 20 and sexo in 'Mm':
            contm += 1
    else:
        print('\033[31mSexo inválido, tente novamente!\033[m')
        break

print('Analizando dados...')
sleep(3)

print('''
A média da idade do grupo é: {}
O Homem mais velho é o {}
E {} mulher/res tem menos de 20 anos de idade.
'''.format(media/4, nomeh, contm))

