nota1 = nota2 = cont = 0
dados = []
while True:
    nome = str(input('Nome do aluno: ')).strip()
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    dados.append([cont, nome, [nota1, nota2]])
    cont += 1
    while True:
        continuar = str(input('\033[33mQuer continuar? [S/N]: \033[m')).strip().upper()[0]
        if continuar in 'SN':
            break
    if 'N' in continuar:
        break
print('-='*50)
print('No. NOME           MÉDIA    ')
print('-'*28)
for a in dados:
    print(f'{a[0]:<4}{a[1]:<15}{(a[2][0] + a[2][1]) / 2:<9.1f}')
print('-'*28)
while True:
    req = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if req == 999:
        break
    print(f'Notas de {dados[req][1]} são {dados[req][2]}')
    print('-'*40)
