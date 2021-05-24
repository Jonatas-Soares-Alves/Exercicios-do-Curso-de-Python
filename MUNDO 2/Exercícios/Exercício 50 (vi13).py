cont = 0
for c in range(0, 6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        cont += n

print('A soma de todos os números PARES digitados é: {}'.format(cont))
