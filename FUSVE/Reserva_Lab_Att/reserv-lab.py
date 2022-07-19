#arquivo com as funções
from funcoes import *

#loop infinito que ocorre o programa
while True:
    #função de limpar feita no arquivo funcoes.py
    limpar()
    print('''
        [ 0 ] - Sair
        [ 1 ] - Consultar
        [ 2 ] - Cadastrar usuário
        [ 3 ] - Gerenciar laboratórios
        [ 4 ] - Login
        [ 5 ] - Agendar
        [ 6 ] - Zerar agendamentos
    ''')
    op = int (input('Selecione uma opção: '))
    #de acordo com a valor da variável op(opção) é acionada uma função
    if op == 0:
        break
    if op == 1:
        consulta()
    if op == 2:
        cadastrar_usuario()
    if op == 3:
        gerenciar_lab()
    if op == 4:
        login()
    if op == 5:
        agendar()
    if op == 6:
        zerar()