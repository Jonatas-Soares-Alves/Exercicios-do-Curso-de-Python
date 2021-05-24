from urllib import request

try:
    page = request.urlopen('http://pudim.com.br/')
except:
    print('\033[31mA página do Pudim NÃO está acessível!\033[m')
else:
    print('\033[32mA página do Pudom ESTÁ acessível!')
