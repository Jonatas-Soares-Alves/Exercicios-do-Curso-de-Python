lista = input('Digite uma expressão com parênteses: ')
if lista.count('(') == lista.count(')'):
    print('\033[32mExpressão aceita\033[m')
else:
    print('\n\033[31mExpressão incorreta!\033[m')
