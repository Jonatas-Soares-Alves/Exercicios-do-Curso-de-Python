l1 = float(input('Digite o comprimento da 1º linha: '))
l2 = float(input('Digite o comprimento da 1º linha: '))
l3 = float(input('Digite o comprimento da 1º linha: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    print('SIM! É possível fazer um triangulo com essas linhas!')
else:
    print('NÃO! Não é possível fazer um triangulo com essas linhas!')
