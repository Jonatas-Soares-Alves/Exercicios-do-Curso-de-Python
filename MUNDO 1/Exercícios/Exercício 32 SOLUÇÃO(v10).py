from datetime import date
ano = int(input('Digite um ano qualquer, ou digite "0" para analizar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano {} é BISSEXTO!\033[m'.format(ano))
else:
    print('\033[31mO ano {} NÃO é BISSEXTO!\033[m'.format(ano))
