nome = input('Digite abaixo seu nome completo:\n').strip()

div = nome.split()

print('''
Seu nome: {}
Primeiro nome: {}
Ultimo nome: {}'''.format(nome, div[0], div[-1]))