soma = 0
cont = 0
for c in range(0 , 501, 3):
    print(c)
    soma += c
    cont += 1

print('Fim, total de {} números e a soma total é de {}'.format(cont, soma))
