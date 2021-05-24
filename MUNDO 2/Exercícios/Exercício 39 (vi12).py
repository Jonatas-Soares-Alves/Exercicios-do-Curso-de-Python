from datetime import date

nasc = int(input('Digite o ano em que nasceu: '))

ano = date.today().year
idade = ano - nasc

if idade < 18:
    print('''
    \033[32mVocê tem {} anos, portanto ainda vai se alistar!
    Falta/am {} ano/os Será em {}!\033[m'''.format(idade, 18 - idade, ano + (18 - idade)))
elif idade > 18:
    print('''
    \033[31mVocê tem {} anos, portanto já passou o tempo de se alistar!
    Atrasou {} ano/os! Foi em {}!\033[m'''.format(idade, idade - 18, ano - (idade - 18)))
else:
    print('''
    \033[33mVocê já tem {} anos! E esse é o ano que você deve se alistar!
    Boa sorte!\033[m'''.format(idade))
