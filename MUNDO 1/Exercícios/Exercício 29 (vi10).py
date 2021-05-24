velo = float(input('\n\033[1;34mA quantos Km/h seu carro está rodando?\033[m\n'))

if velo > 80:
    multa = float((velo - 80) * 7)
    print('\n\033[4;31mVocê foi multado!\033[0;31m A multa é de \033[1;33mR${:.2f}\033[m'.format(multa))
else:
    print('\n\033[4;32mVocê está dentro do limite de velocidade!\033[0;32m Sem problemas.')
