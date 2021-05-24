nome = input('Digite o seu nome completo:\n').strip()

nome2 = nome.upper()
print('Seu nome todo em MAIUSCULO:\n{}\n'.format(nome2))

nome3 = nome.lower()
print('Seu nome todo em minusculo:\n{}\n'.format(nome3))

nome4 = len(nome) - nome.count(' ')
print('Seu nome tem um total de {} letras\n'.format(nome4))

nome5 = nome.split()
print('Seu primeiro nome tem {} letras\n'.format(len(nome5[0])))
