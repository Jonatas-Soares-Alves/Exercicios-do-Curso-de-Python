valores = list()
while True:
    n = int(input('\n\033[35mDigite um valor: \033[m'))
    if n in valores:
        print('\n\033[31mValor repetido, não pode ser registrado!\033[m')
    else:
        valores.append(n)

    while True:
        continuar = str(input('\n\033[33mQuer continuar? [S/N]: \033[m')).strip().upper()[0]
        if continuar in 'SN':
            break
    if 'N' in continuar:
        break
print(sorted(valores))
