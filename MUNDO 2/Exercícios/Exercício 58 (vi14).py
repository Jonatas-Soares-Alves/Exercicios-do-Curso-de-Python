from random import randint

com = randint(1, 10)
tent = 0
user = 0

while com != user:
    user = int(input('\nAdvinhe o número (1 até 10): '))
    print('\nErrado! Tente novamente!')
    tent += 1

print('''
Parabéns! Você Advinhou!
Comp = {}
Você = {}
Tentativas = {}
'''.format(com, user, tent))
