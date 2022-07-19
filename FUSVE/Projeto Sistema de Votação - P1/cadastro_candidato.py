arq = open('candidatos.txt', 'a')


while True:
    print('[ 1 ] --> Cadastrar\n[ 2 ] --> Sair')

    op = int (input('\n[ # ]--> '))

    if op == 2:
        exit()

    nome = input('Nome do candidato: ')

    numero = int (input('Número do candidato: '))

    arq.write(f'{nome} {numero}\n')