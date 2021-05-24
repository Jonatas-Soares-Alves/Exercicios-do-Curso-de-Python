dec = int(input('\n{}Digite um número decimal inteiro: {}'.format('\033[35m', '\033[m')))
conv = int(input('''
{}Escolha a base da conversão:{}
{}[ 1 ] - para binário{}
{}[ 2 ] - para octal{}
{}[ 3 ] - para hexadecimal{}

'''.format('\033[35m', '\033[m',
           '\033[31m', '\033[m',
           '\033[34m', '\033[m',
           '\033[32m', '\033[m')))

if conv == 1:
    print('{} convertido para BINÁRIO é {}'.format(dec, bin(dec)[2:]))
elif conv == 2:
    print('{} convertido para OCTAL é {}'.format(dec, oct(dec)[2:]))
elif conv == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(dec, hex(dec)[2:]))
else:
    print('Número inválido')
