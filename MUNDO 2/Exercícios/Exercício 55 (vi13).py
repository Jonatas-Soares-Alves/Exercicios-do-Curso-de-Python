maior = 0
menor = 0

for l in range(0, 5):
    peso = float(input('\nDigite o peso da {}º pessoa: '.format(l + 1)))
    if l == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('\nO maior peso registrado foi: {:.2f}Kg\nE o menor foi {:.2f}Kg'.format(maior, menor))