def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    maior = menor = tot = soma = 0
    for p, a in enumerate(n):
        tot += 1
        soma += a
        if p == 0:
            maior = menor = a
        else:
            if a > maior:
                maior = a
            elif a < menor:
                menor = a
    media = soma / tot
    analise = {'total': tot, 'maior': maior, 'menor': menor, 'média': media}
    if sit:
        if media >= 7:
            analise['situação'] = 'BOA'
        elif 6 <= media < 7:
            analise['situação'] = 'RAZOAVEL'
        else:
            analise['situação'] = 'RUIM'
    return analise


resp = notas(3.5, 10, 6.5, 10, 8,  sit=True)
print(resp)
