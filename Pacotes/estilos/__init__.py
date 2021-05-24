def clean():
    return '\033[m'


def stclean():
    return '\033[0m'


def stbold():
    return '\033[1m'


def stunder():
    return '\033[4m'


def stnegative():
    return '\033[7m'


def txwhite():
    return '\033[30m'


def txred():
    return '\033[31m'


def txgreen():
    return '\033[32m'


def txyellow():
    return '\033[33m'


def txblue():
    return '\033[34m'


def txpurple():
    return '\033[35m'


def txcian():
    return '\033[36m'


def txgray():
    return '\033[37m'


def bkwhite():
    return '\033[40m'


def bkred():
    return '\033[41m'


def bkgreen():
    return '\033[42m'


def bkyellow():
    return '\033[43m'


def bkblue():
    return '\033[44m'


def bkpurple():
    return '\033[45m'


def bkcian():
    return '\033[46m'


def bkgray():
    return '\033[47m'


def linha(tam=50):
    print(f'{txgray()}-' * tam + f'{clean()}')


def stmenu(msg='MENU', tam=50):
    print(f'{stbold()}-' * tam)
    print(f'{msg}'.center(tam))
    linha()


def stoptions(num=1, txt='Opção 1'):
    print(f'{stbold()}{txyellow()}{num} {txgray()}- {txblue()}{txt}')


def resp():
    return f'{stbold()}{txyellow()}Sua Opção:{clean()} '

