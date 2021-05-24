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
print(dados)
