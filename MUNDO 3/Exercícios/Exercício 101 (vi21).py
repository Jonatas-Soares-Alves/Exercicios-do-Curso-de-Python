def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if 18 <= idade <= 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO NEGADO!'


print(voto(2000))
