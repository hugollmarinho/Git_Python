#name usado para saber o sistema, system usado para fazer comando de prompt e stat usado para saber tamanho de arquivos
from os import name, system, stat
#sleep usado para conggelar o código
from time import sleep

def consulta():
#exibe as reservas
    limpar()
    try:
        #abre o arquivo no modo leitura e analisa o tamanho
        arq = open('reservas.txt', 'r')
        if stat('reservas.txt').st_size == 0:
            print('Sem reservas feitas')
            sleep(5)
            #se o tamanho for igual a 0 bytes ou o arquivo não existir, será exibida uma mensagem
        else:
            for linha in arq:
                print(linha)
            sleep(5)
    except:
        print('Sem reservas')
        sleep(5)

def cadastrar_usuario():
#adiciona novos usuários no arquivo
    limpar()
    if login == False:
        print('Necessário estar logado')
    else:
        arq2 = open('usuarios.txt', 'a')
        nome = input('Nome: ')
        senha = input('Senha: ')
        #escreve os usuários no arquivo txt
        arq2.write(f'{nome} | {senha} | \n')
        print("Cadastro bem sucedido")
    sleep(5)

def login():
	#se as variáveis nome e senha estiverem no arquivo txt, o login será efetuado e a variável 'logado' será verdadeira (True)
    global logado
    limpar()
    arq2 = open('usuarios.txt', 'r')
    nome = input('Nome: ')
    senha = input('Senha: ')
    dados = []
    for linha in arq2: 
        dados.append(linha.split(' | ')[0])
        dados.append(linha.split(' | ')[1])
    if nome in dados and senha in dados:
        print('Login Bem Sucedido')
        logado = True
    else:
        print('Falha no Login')
    sleep(5)

def gerenciar_lab():
    limpar()
    if logado == False:
        print("Necessário estar logado")
    else:
        #abre o arquivo dos laboratórios em modo leitura
        arq3 = open('lab.txt', 'r')
        #duas listas que armazenam os laboraŕios (lab1, lab2, lab3, lab4) e seu status (aberto/fechado)
        labs = []
        status = []
        for linha in arq3:
            print(linha)
            labs.append(linha.split(' - ')[0])
            status.append(linha.split(' - ')[1])
        #abre o arquivo no modo atualização
        arq3 = open('lab.txt', 'a')
        op = int (input('Selecione um laboratório [1, 2, 3, 4]: '))
        estado = int(input('Selecione um status [1 - aberto / 2 - fechado]: '))
        #muda o estado dos laboratórios
        if estado == 1:
            status[op - 1] = 'Aberto \n'
        if estado == 2:
            status[op - 1] = 'Fechado \n'
        #limpa o arquivo e escreve tudo novamente, porém com atualizações
        arq3 = open('lab.txt', 'w')
        for cont in range(0, 4):
            arq3.write(f'{labs[cont]} - {status[cont]}')
        print('Mudanças aplicadas')
    sleep(5)

def agendar():
	#exibe os laboratórios abertos e fechados e permite que mude o status deles
    limpar()
    if logado == False:
        print('Necessário estar logado')
    else:
        arq3 = open('lab.txt', 'r')
        for linha in arq3:
            print(linha)
        #entrada e escrita de informações no arquivo de reservas
        lb = int(input('Selecione um laboratório [1, 2, 3, 4]: '))
        inicio = input('Digite o horário de início: ')
        fim = input("Digite o horário do fim: ")
        arq3 = open('reservas.txt', 'a')
        arq3.write(f'lab{lb} | {inicio} | {fim} \n')
        print('Horário reservado')
    sleep(5)

def zerar():
	#função que abre o arquivo de reservas e dixa ele vazio
    limpar()
    arq3 = open('reservas.txt', 'w')
    print('Reservas zeradas')
    sleep(5)

#=====================#

#função de limpar tela (se o sistema for 'nt'(windows) ele usará o comando 'cls', caso não seja, usará o comando 'clear')

def limpar():
    if name == 'nt':
        limpar = 'cls'
    else:
        limpar = 'clear'
    system(limpar)
    
#Variável que valida se o login foi feito
logado = False
