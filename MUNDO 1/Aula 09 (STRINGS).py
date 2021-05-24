#teste de seleção de Strings

f1 = 'Curso em Vídeo Python'

print('1 -', f1[6])       #Escolhe uma letra.

print('2 -', f1[9:13])    #Escolhe de uma seleção a outra, menos a ultima letra.

print('3 -', f1[:13])     #Escolhe do começo até a letra descrita.

print('4 -', f1[13:])     #Escolhe da seleção até o final.

print('5 -', f1[9:15:2])  #Escolhe um intervalo com espaçamento de 2.

print('6 -', f1[::2])     #Seleciona toda a String com o espaçamento de 2

#Funções:

print('7 -', f1.count('o'))     #Conta as letras "o" minusculo

print('8 -', f1.upper().count('O'))  #Passa todas as letras para MAIUSCULO e conta todos os "O" MAIUSCULO

print('9 -', len(f1))  #Conta o tamanho da frase

#Length e Frase 2

f2 = '   Curso em Vídeo Python   ' #Mesma frase porém com espaços pois eles contam

print('10 -', len(f2)) #contando até os espaços

print('11 -', len(f2.strip())) #Tira os espaços no começo e no fim da frase

# f2.rstrip retira espaços do lado direito, e .lstrip do esquerdo.

#Replace com a Frase 1

print('12 -', f1.replace('Python', 'Android')) #Troca parte da String

#Ou

f1 = f1.replace('Python', 'Android') #Troca parte da String e atribui o valor.
print('13 -', f1)

#Verificação

print('14 - V')
print('Curso' in f1) #Verifica se "Curso" está na frase

print('15 - V')
print(f1.find('Vídeo')) #Procura onde está a sequencia "Vídeo" na frase e indica onde começa
#Caso não encontre aparecerá "-1"

#Split

f1 = f1.split() #Divide a frase pelos espaços e atribuiu.

print('16 -', f1) #Como fica

print('17 -', f1[0]) #Selecionando apenas a primeira palavras

print('18 -', f1[0][3]) #Seçeciona a palavra e a letra da palavra escolhida

#Junção

print('19 -', '-'.join(f1)) #Junta as palavras com o caractere (-)

print('20 -', ' '.join(f1)) #Junta as palavras com espaço

print('21 -', ''.join(f1)) #Junta as palavras.
