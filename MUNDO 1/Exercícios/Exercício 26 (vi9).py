f = input('Digite uma frase qualquer:\n').strip().upper()

print('''
A letra "A" apareceu {} vezes.
A primiera aparição da letra "A" foi na posição {}.
E a ultima na posição {}'''.format(f.count('A'), f.find('A')+1, f.rfind('A')+1))
