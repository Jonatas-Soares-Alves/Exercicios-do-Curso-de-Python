cont = maiores = homens = mulheres = 0
while True:
    cont += 1
    print('\033[33m' + '#=' * 20 + '\033[m')
    print(f'\033[0:35mRegistro da {cont}º pessoa:\033[m')

    #======================IDADE========================
    while True:
        idade = int(input('Digite a idade: '))

        if idade < 0:
            print('\033[31mDado inválido!\033[m')
        else:
            break

    if idade >= 18:
        maiores += 1
    #======================IDADE========================

    #=======================SEXO========================
    while True:
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

        if sexo in 'MF':
            break
        else:
            print('\033[31mDado inválido!\033[m')
    print('\033[33m' + '#=' * 20 + '\033[m')

    if sexo in 'M':
        homens += 1
    elif idade < 20 and sexo in 'F':
        mulheres += 1
    #=======================SEXO========================

    #=====================CONTINUAR=====================
    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

        if continuar in 'NS':
            break
        else:
            print('\033[31mDado inválido!\033[m')

    if continuar in 'N':
        break
    #=====================CONTINUAR=====================

print(f'''\033[32mCOMCLUSÃO DOS DADOS
\033[33m{maiores}\033[32m pessoas tem mais de 18 anos.
\033[33m{homens}\033[32m homens foram cadastrados.
\033[33m{mulheres}\033[32m mulheres tem menos de 20 anos.
        ''')
