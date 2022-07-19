arq = open('eleitores.txt', 'a')

while True:
    print('[ 1 ] --> cadastrar\n[ 2 ] --> sair')

    op = int(input('\n[ # ]--> '))

    if op == 2:
        exit()

    nome = input('Nome: ')
    matricula = input('matricula: ')
    arq.write(f'{matricula} {nome} ')