n = int(input('Digite um número para ser fatorizado: '))
cont = n
for f in range(n - 1, 0, -1):
    cont = cont * f

print("O fatorial de {} é: {}".format(n, cont))
