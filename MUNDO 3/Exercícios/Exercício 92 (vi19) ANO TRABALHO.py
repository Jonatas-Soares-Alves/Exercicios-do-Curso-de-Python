from _datetime import date
dados = {}
atual = date.today().year
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
dados['idade'] = atual - ano
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (35 - (atual - dados['contratação']))

print('\n', dados)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
