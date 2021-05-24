n = int(input('Digite um número para ser fatorizado: '))
f = n
n1 = n - 1
while n1 != 1:
    f *= n1
    n1 -= 1

print('{} fatorial é igual a {}'.format(n, f))
