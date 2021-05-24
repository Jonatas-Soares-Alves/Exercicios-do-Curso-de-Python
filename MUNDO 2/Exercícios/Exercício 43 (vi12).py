#IMC = 80 kg ÷ (1,80 m × 1,80 m) = 24,69 kg/m2 (Peso ideal)

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está \033[33mABAIXO DO PESO!\033[m')

elif imc >= 18.5 and imc < 25:
    print('Você está \033[32mNO PESO IDEIAL!\033[m')

elif imc >= 25 and imc < 30:
    print('Você está \033[33mCOM SOBREPESO!\033[m')

elif imc >= 30 and imc < 40:
    print('Você está \033[31mCOM OBESIDADE!\033[m')

else:
    print('Você está \033[7:31mCOM OBESIDADE MÓRBIDA!\033[m')
