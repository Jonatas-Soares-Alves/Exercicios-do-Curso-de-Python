frase = input('\n\033[36mEscreva uma frase:\033[m\n').strip().upper()

f = frase.split()
f = ''.join(f)
pol = ''

for c in range(len(f) - 1, -1, -1):
    pol += f[c]

print('\033[32mA frase: \033[33m"{}"\033[32m ao contrário fica \033[33m"{}"\033[m'.format(f, pol))

if f == pol:
    print('''
    \033[32mÉ um Palindromo!\033[m
    ''')
else:
    print('''
    \033[31mNÃO é um Palindromo!\033[m
    ''')

