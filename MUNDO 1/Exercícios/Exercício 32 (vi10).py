ano = int(input('Digite um ano para verificação: '))

dez = ano % 100

if dez == 0:
    cent = ano % 1000
    cent = cent % 400

    if cent == 0:
        print('\n{} é ano bissexto!'.format(ano))
    else:
        print('\n{} não é ano bissexto!'.format(ano))

else:
    dez = dez % 4

    if dez == 0:
        print('\n{} é ano bissexto!'.format(ano))
    else:
        print('\n{} não é ano bissexto!'.format(ano))