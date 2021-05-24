user = 0

n1 = int(input('\nDigite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

while user != 5:
    user = int(input('''
Escolha uma opção:
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos Números
[ 5 ] - Sair do programa
'''))
    if user == 1:
        print('\n{} + {} = {}'.format(n1, n2, n1 + n2))
    elif user == 2:
        print('\n{} x {} = {}'.format(n1, n2, n1 * n2))
    elif user == 3:
        if n1 > n2:
            print('\nO 1º valor "{}" é maior que o 2º valor "{}"'.format(n1, n2))
        elif n1 < n2:
            print('\nO 2º valor "{}" é maior que o 1º valor "{}"'.format(n2, n1))
        else:
            print('\nOs dois valores são iguais!')
    elif user == 4:
        n1 = int(input('\nDigite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    else:
        print('\nNúmero inválido, tente novamente!')

print('\nPrograma filanizado!')