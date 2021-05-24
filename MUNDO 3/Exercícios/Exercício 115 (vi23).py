import estilos
from dado import leiaint

while True:
    try:
        dados = open('pessoas.txt', 'a+')
        estilos.stmenu('MENU PRINCIPAL')
        estilos.stoptions(1, 'Ver pessoas Cadastradas')
        estilos.stoptions(2, 'Cadastrar nova Pessoa')
        estilos.stoptions(3, 'Sair do Sistema')
        estilos.linha()
        res = leiaint(estilos.resp())

        if 1 <= res <= 3:
            if res == 1:
                estilos.stmenu('OPÇÃO 1')
                dados = open('pessoas.txt', 'r')
                print(dados.read())

            elif res == 2:
                estilos.stmenu('OPÇÃO 2')
                dados = open('pessoas.txt', 'a+')
                nome = input('Nome: ').strip()
                idade = leiaint('Idade: ')
                cad = f'{nome:<40}' + f'{idade:<10}\n'
                dados.write(cad)


            elif res == 3:
                dados.close()
                break
        else:
            print(f'{estilos.stbold()}{estilos.txred()}Por favor digite uma opção válida!{estilos.clean()}')

    except Exception as erro:
        print(f'{estilos.stbold()}{estilos.txred()}Um ERRO aconteceu no sistema!{estilos.clean()}')
        print('Erro:', erro.__cause__)

