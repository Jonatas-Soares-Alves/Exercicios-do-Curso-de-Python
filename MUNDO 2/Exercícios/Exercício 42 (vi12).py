l1 = float(input('Digite o comprimento da 1º linha: '))
l2 = float(input('Digite o comprimento da 2º linha: '))
l3 = float(input('Digite o comprimento da 3º linha: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    print('\033[32mSIM! É possível fazer um triangulo com essas linhas!\033[m')

    if l1 == l2 == l3:
        print('E ele é um \033[33mTRIÂNGULO E!\033[m')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('E ele é um \033[33mTRIÂNGULO RETANGULO!\033[m')
    else:
        print('E ele é um \033[33mTRIÂNGULO ESCALENO!\033[m')

else:
    print('\033[31mNÃO! Não é possível fazer um triangulo com essas linhas\033[m!')
