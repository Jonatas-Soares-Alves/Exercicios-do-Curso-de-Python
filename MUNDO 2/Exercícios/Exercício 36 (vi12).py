val = float(input('\n\033[35mQual o preço da casa? R$'))
sal = float(input('\n\033[35mQual o seu salário atual? R$'))
anos = float(input('\n\033[35mEm quantos anos vai pagar?'))

parcelas = val / (anos * 12)

print('\n\033[36mTodo mês você terá que pagar \033[4;33mR${:.2f}\033[0;36m para pagar a casa!'.format(parcelas))

if parcelas > (sal * 0.3):
    print('''
    \033[31mMas infelizmente as parcelas excedem o limite de \033[33m30%\033[31m de seu salário.
    Por tanto você \033[1mNÃO\033[0;31m poderá compra-la.''')
else:
    print('''
    \033[32mAs parcelas estão dentro do limite de \033[33m30%\033[32m de seu salário.
    \033[1mParabéns pela sua nova aquizição!\033[m''')
