from datetime import date

nasc = int(input('\nQual seu ano de nascimento? '))
ano = date.today().year
idade = ano - nasc

print('\n\033[36mSua categoria é:\033[m')
if idade <= 9:
    print('\033[33mMIRIM!\033[m')
elif idade <= 14:
    print('\033[33mINFANTIL!\033[m')
elif idade <= 19:
    print('\033[33mJUNIOR!\033[m')
elif idade <= 25:
    print('\033[33mSÊNIOR!\033[m')
else:
    print('\033[33mMASTER!\033[m')
