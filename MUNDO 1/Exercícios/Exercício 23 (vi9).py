#n = input('Digite um número de quatro digitos de 0001 até 9999: ').split()

#print('''Seu número:
#Unidade: {}
#Dezena: {}
#Centena: {}
#Milhar: {}
#'''.format(n[3], n[2], n[1], n[0]))

#PRECISA SABER ESTRUTURA DE LOOP ^

#Tentativa minha:

m = int(input('Digite um número de quatro digitos de 0001 até 9999: '))

m1 = m // 1000
m2 = (m - m1 * 1000) // 100
m3 = (m - (m2 * 100 + m1 * 1000)) // 10
m4 = (m - (m3 * 10 + m2 * 100 + m1 * 1000))

print('''Seu número:
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}

Resposta 2:
'''.format(m4, m3, m2, m1))

#Resposta mais curta

r1 = m // 1 % 10
r2 = m // 10 % 10
r3 = m // 100 % 10
r4 = m // 1000 % 10

print('''Seu número:
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}

Resposta 2:
'''.format(r1, r2, r3, r4))