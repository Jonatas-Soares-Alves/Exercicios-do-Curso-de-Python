n1 = float(input('Digite sua 1º nota: '))
n2 = float(input('Digite sua 2º nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('\033[31mREPROVADO!\033[m')
elif media > 5 and media < 6.9:
    print('\033[33mRECUPERAÇÃO!\033[m')
else:
    print('\033[32mAPROVADO!\033[m')
