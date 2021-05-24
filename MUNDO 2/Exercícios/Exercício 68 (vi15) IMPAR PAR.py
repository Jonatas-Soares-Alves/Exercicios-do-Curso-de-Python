from random import randint
vit = 0
while True:
    comp = randint(0, 10)

    while True:
        print('#=' * 40)
        jog = int(input('\033[36mVÁMOS JOGAR PAR OU IMPAR! Primeiro escolha um número de 0 á 10 para jogar!\nSeu número: \033[m'))
        if jog > 10 or jog < 0:
            print('\033[31mNúmero inválido! Tente novamente!\033[m')
        else:
            break

    while True:
        print('#=' * 40)
        imppar = input('\033[35mAgora escolha impar ou par [I/P]: \033[m').strip().upper()[0]
        if imppar in 'IP':
            break
        else:
            print('\033[31mValor inválido! Tente novamente!\033[m')
    print('#=' * 40)

#=================================VITORIA
    if imppar in 'P' and (comp + jog) % 2 == 0:
        print(f'''\033[1:32mVOCÊ GANHOU!\033[0:32m
O computador escolheu: \033[33m{comp}\033[32m
Você jogou: \033[33m{jog}\033[32m
Escolheu: \033[33m{imppar}\033[32m
E \033[33m{comp}\033[32m + \033[33m{jog}\033[32m = \033[33m{comp + jog}\033[32m que é \033[1:33mPAR!\033[m''')
        vit += 1

    elif imppar in 'I' and (comp + jog) % 2 != 0:
        print(f'''\033[1:32mVOCÊ GANHOU!\033[0:32m
O computador escolheu: \033[33m{comp}\033[32m
Você jogou: \033[33m{jog}\033[32m
Escolheu: \033[33m{imppar}\033[32m
E \033[33m{comp}\033[32m + \033[33m{jog}\033[32m = \033[33m{comp + jog}\033[32m que é \033[1:33mIMPAR!\033[m''')
        vit += 1
# =================================VITORIA

# =================================DERROTA

    elif imppar in 'P' and (comp + jog) % 2 != 0:
        print(f'''\033[1:31mVOCÊ PERDEU!\033[0:31m
O computador escolheu: \033[33m{comp}\033[31m
Você jogou: \033[33m{jog}\033[31m
Escolheu: \033[33m{imppar}\033[31m
E \033[33m{comp}\033[31m + \033[33m{jog}\033[31m = \033[33m{comp + jog}\033[31m que NÃO é \033[1:33mPAR!\033[m
''')
        break

    elif imppar in 'I' and (comp + jog) % 2 == 0:
        print(f'''\033[1:31mVOCÊ PERDEU!\033[0:31m
O computador escolheu: \033[33m{comp}\033[31m
Você jogou: \033[33m{jog}\033[31m
Escolheu: \033[33m{imppar}\033[31m
E \033[33m{comp}\033[31m + \033[33m{jog}\033[31m = \033[33m{comp + jog}\033[31m que NÃO é \033[1:33mIMPAR!\033[m
''')
        break
# =================================DERROTA
print(f'\033[33mTotal de vitórias: {vit}\033[m')
print('\033[33mObrigado por Jogar!\033[m')
