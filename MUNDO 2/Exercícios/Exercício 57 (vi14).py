sexo = input('Digite seu sexo [M/F]: ').upper().strip()
while sexo not in 'MmFf':
    sexo = input('\nSexo inválido! Digite seu sexo [M/F]: ').strip().upper()[0]
print('\nSexo {} registrado com sucesso!'.format(sexo))
