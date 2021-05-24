clubs = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Palmeiras', 'Grêmio',
         'Corinthians', 'Bragantino', 'Santos', 'Athletico-PR', 'Atlético-GO', 'Ceará SC', 'Sport Recife', 'Fortaleza',
         'Bahia', 'Vasco da Gama', 'Coritiba', 'Botafogo')

print(f'\nOs 5 primeiros colocados são: {clubs[0:5]}')
print(f'\nOs últimos 4 colocados são: {clubs[15:]}')
print(f'\nOs times em ordem alfabética: {sorted(clubs)}')

if clubs.count('Chapecoense') > 0:
    print(f'\nA Chapecoence está na {clubs.index("Chapecoense") + 1}º posição')
else:
    print('\nO time da Chapecoense não está entre os 20 classificados.')
