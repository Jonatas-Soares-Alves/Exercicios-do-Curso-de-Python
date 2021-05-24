def area(lar, comp):
    print(f'A área de um terreno {lar:.1f}x{comp:.1f} é de {lar*comp:.1f}m²')


print('Controle de Terrenos')
print('-'*30)
lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(lar, comp)
