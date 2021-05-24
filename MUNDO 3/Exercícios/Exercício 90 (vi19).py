aluno = {'Nome': str(input('Digite seu nome: ')),
         'Média': float(input('Digite a média de : '))}
if aluno['Média'] >= 7:
    aluno['Resultado'] = 'Aprovado!'
else:
    aluno['Resultado'] = 'Reprovado'

print(f'''Nome: {aluno['Nome']}
Média: {aluno['Média']:.1f}
Situação: {aluno['Resultado']}
''')
