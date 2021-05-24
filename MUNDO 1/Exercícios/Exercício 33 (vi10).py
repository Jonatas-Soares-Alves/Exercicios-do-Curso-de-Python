n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

#MAIOR NÚMERO
if n1 >= n2 and n1 >= n3:
    print('\nO maior número é {}'.format(n1))

elif n2 >= n1 and n2 >= n3:
    print('\nO maior número é {}'.format(n2))

elif n3 >= n1 and n3 >= n2:
    print('\nO maior número é {}'.format(n3))
#MAIOR NÚMERO

#menor número
if n1 <= n2 and n1 <= n3:
    print('\nE o menor número é {}'.format(n1))

elif n2 <= n1 and n2 <= n3:
    print('\nE o menor número é {}'.format(n2))

elif n3 <= n1 and n3 <= n2:
    print('\nE o menor número é {}'.format(n3))
#menor número
