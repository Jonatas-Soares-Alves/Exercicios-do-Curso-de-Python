#Fn = Fn - 1 + Fn - 2
# 1 - 1 - 2 - 3 - 5
n = int(input('\nDigite um número inteiro: '))
qnt = int(input('Quantos elementos quer que apareça? '))

print('{} '.format(n),end='')

if n == 0:
    print('1 1 ',end='')
    n = 1

n1 = n
n = n + n
n2 = n
while qnt != 1:
    print('{} '.format(n),end='')
    n = n1 + n2
    n1 = n2
    n2 = n
    qnt += -1

print('\nFim da sequência.')
