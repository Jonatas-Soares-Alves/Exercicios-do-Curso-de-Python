preco = float(input('\n\033[36mQual o preço do produto que pretende comprar? R$'))
pag = int(input('''
Como pretende pagar?\033[m

\033[1:33m[ 1 ] - \033[0:35mÀ vista DINHEIRO/CHEQUE: \033[32m10% de desconto!\033[m
\033[1:33m[ 2 ] - \033[0:35mÀ vista no CARTÃO: \033[32m5% de desconto\033[m
\033[1:33m[ 3 ] - \033[0:35mEm até 2x NO CARTÃO: \033[33mPreço normal\033[m
\033[1:33m[ 4 ] - \033[0:35m3x ou mais no CARTÃO: \033[31m20% de juros\033[m
'''))

if pag == 1:
    print('''
    \033[36mPreço Nomal: R${:.2f}
    \033[35mForma de pagamento: À vista DINHEIRO/CHEQUE
    \033[32mDesconto: 10%
    \033[1:33mTotal: R${:.2f}\033[m
    '''.format(preco, preco * 0.9))
elif pag == 2:
    print('''
    \033[36mPreço Nomal: R${:.2f}
    \033[35mForma de pagamento: À vista no CARTÃO
    \033[32mDesconto: 5%
    \033[1:33mTotal: R${:.2f}\033[m
    '''.format(preco, preco * 0.95))
elif pag == 3:
    print('''
    \033[36mPreço Nomal: R${:.2f}
    \033[35mForma de pagamento: Até 2x no CARTÃO
    \033[35mParcelas: 2 parcelas de R${}
    \033[33mDesconto: 0% (Preço normal)
    \033[1:33mTotal: R${:.2f}\033[m
    '''.format(preco, preco/2, preco))
elif pag == 4:
    parc = int(input('\033[36mQuantas parcelas?\033[m '))
    print('''
    \033[36mPreço Nomal: R${:.2f}
    \033[35mForma de pagamento: {}x no CARTÃO
    \033[35mParcelas: {} parcelas de R${}
    \033[31mJuros: 20%
    \033[1:33mTotal: R${:.2f}\033[m
    '''.format(preco, parc, parc, preco/parc, preco * 1.20))
else:
    print('\033[7:31mNÚMERO INVÁLIDO!!!\033[m')
