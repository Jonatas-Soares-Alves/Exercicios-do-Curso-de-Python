n = 0
cont = 0
continua = 'S'
maior = menor = 0
soma = 0

while continua == 'S':
    n = int(input('\nDigite um número inteiro: '))
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    cont += +1
    soma += n

    continua = input('Quer continuar? [S/N]: ').strip().upper()

print('''
Dados:
Você Digitou {} números.
O maior número foi {}
O menor nùmero foi {}
E a média entre eles é {}
'''.format(cont, maior, menor, soma/cont))
