def leiaInt(txt):
    while True:
        num = str(input(txt)).strip()
        v = True
        if len(num) == 0:
            num = 'n'
        for n in num:
            if n not in '0123456789':
                print('\033[31mERRO! Digite um número inteiro válido!\033[m')
                v = False
                break
        if v:
            num = int(num)
            break
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
