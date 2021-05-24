lista = []
while True:
    lista.append(int((input('\nDigite um número: '))))

    while True:
        continuar = str(input('\nContinuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'NS':
            break
        else:
            print('\nNúmero inválido!')
    if continuar in 'N':
        break
lista.sort(reverse=True)
print(f'''
{len(lista)} Números registrados
Lista em ordem decrescente: {lista}''')
print('O valor 5 está na lista' if 5 in lista else 'O valor 5 não está na lista')
