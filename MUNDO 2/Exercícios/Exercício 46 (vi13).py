from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\033[7:31m*-#-\033[m'*20)
print('\033[7:33m{:*^80}\033[m'.format(' BOOM '))
print('\033[7:31m*-#-\033[m'*20)
