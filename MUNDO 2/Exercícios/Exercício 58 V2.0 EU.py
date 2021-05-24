from random import randint

com = randint(0, 10)
tent = 0
user = 0

while com != user:
    user = int(input('\nAdvinhe o número (0 até 10): '))
    tent += 1
    if user > com:
        print('Valor alto!')
    elif user < com:
        print('Valor baixo!')

print('''
Parabéns! Você Advinhou!
Comp = {}
Você = {}
Tentativas = {}
'''.format(com, user, tent))
