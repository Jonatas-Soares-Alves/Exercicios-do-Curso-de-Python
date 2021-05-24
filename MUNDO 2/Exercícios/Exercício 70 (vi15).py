cont = total = mil = barato = 0
nomeb = ''
while True:
    nome = str(input('\nDigite o NOME do produto: ')).strip().upper()
    preco = int(input('\nDigite o PREÇO do produto: R$'))

    cont += 1
    total += preco

    if cont == 1 or preco < barato:
        barato = preco
        nomeb = nome

    if preco > 1000:
        mil += 1

    # CONTINUAR
    while True:
        continuar = str(input('\nQuer continuar? [S/N]: ')).strip().upper()

        if continuar in 'SN':
            break
        else:
            print('\n\033[31mValor inválido! tente novamente!\033[m')
    if continuar in 'N':
        break
    # CONTINUAR

print(f'''
    Itens comprados: {cont}
    Total gasto: R${total:.2f}
    Intens acima de R$1000.00: {mil}
    Nome do item mais barato foi a {nomeb} custando R${barato::.2f}
    ''')
