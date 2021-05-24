palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for termo in palavras:
    print(f'\nNa palavra {termo} temos: ', end='')
    for c in range(0, len(termo)):
        print(f'{termo[c]} 'if termo[c] in 'aeiou' else '', end='')
