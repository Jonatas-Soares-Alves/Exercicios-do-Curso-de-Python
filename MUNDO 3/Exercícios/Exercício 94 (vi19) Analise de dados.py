pessoa = dict()
grupo = list()
total = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Idade: '))
    total += pessoa['idade']
    grupo.append(pessoa.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
media = total/len(grupo)
print('\n', grupo)

print(f'''
- O grupo tem {len(grupo)} pessoas.
- A média de idade é de {media:.2f} anos.
- As mulheres cadastradas foram: ''', end='')
for p in grupo:
    if 'F' in p['sexo']:
        print(f'{p["nome"]} ', end='')
print('\n- Lista das pessoas que estão acima da média:')
for p in grupo:
    if p['idade'] > media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\n<< ENCERRANDO >>')
