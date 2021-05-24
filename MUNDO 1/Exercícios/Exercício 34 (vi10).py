salario = float(input('Digite o seu salário atual: '))

if salario <= 1250:
    print('\nSeu novo salario com ajuste de +15% é R${:.2f}'.format(salario * 1.15))
else:
    print('\nSeu novo salario com ajuste de +10% é RS{:.2f}'.format(salario * 1.1))
