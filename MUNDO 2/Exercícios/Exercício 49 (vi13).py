n = int(input('Digite um número para calcular a tabuada: '))

for t in range(1, 11):
    print('{} X {} = {}'.format(n, t, n * t))
print('Fim da tabuada')
