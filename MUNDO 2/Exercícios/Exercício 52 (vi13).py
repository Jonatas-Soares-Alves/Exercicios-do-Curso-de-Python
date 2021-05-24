n = int(input('Digite um número inteiro: '))

ver = 0
for c in range(1, n+1):
    res = n % c
    if res == 0:
        res += 1
        ver += res
        print('\033[33m{} '.format(c), end='')
    else:
        print('\033[35m{} '.format(c), end='')

if ver == 2:
    print('\n\033[32m{} É um número primo!\033[m'.format(n))
else:
    print('\n\033[31m{} NÃO é um número primo!\033[m'.format(n))

        
