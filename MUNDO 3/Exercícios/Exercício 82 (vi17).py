lista = []
par = []
imp = []
while True:
    lista.append(int(input('Digite um valor: ')))

    while True:
        continuar = str(input('Continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Valor inválido')
    if 'N' in continuar:
        break

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)

print(f'''
Lista: {lista}
Pares: {par}
Impares: {imp}
''')
