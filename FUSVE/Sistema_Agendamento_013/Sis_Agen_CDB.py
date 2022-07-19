import os
import sqlite3
from sqlite3 import Error

txt_menu_principal = str("CRIAÇÃO DE TABELAS")
n_op_01 = int("01")
n_op_02 = int("02")
n_op_03 = int("03")
txt_inf_1 = str("Universidade de Vassouras - Campus Maricá")
txt_inf_2 = str("Desenvolvido pelo aluno de Engenharia de Software")
txt_inf_3 = str("Hugo Marinho - 2022.1 - Turma A")
txt_inf_4 = str("Pensamento Computacional - Alessandra Alves Fonseca Vargas")
txt_op_consulta = str("Criar Tabela de Agendas.")
txt_op_logar = str("Criar Tabela de Usuarios.")
txt_op_sair = str("Sair.")
txt_sucesso_agendamento = str("Tabela Agendamento Criada.")
txt_sucesso_usuarios = str("Tabela Usuarios Criada.")
txt_sugestao_opc_inv = str("Opção Invalida.")
txt_op_agendamento = str("Tabela Agendamento.")
txt_op_usuarios = str("Tabela Usuarios.")
txt_sucesso_sair = str("MUITO OBRIGADO POR USAR O SISTEMA DE AGENDAMENTO")
txt_interacao_opcao = str("Digite a Opção Desejada: ")


def conecta_banco():
    local = "SIS_BETA.db"
    conec = None
    try:
        conec = sqlite3.connect(local)
    except Error as erro:
        print(f"\t\033[41;97;1m{erro: ^64}\033[0;0m")
    return conec


vcon = conecta_banco()


def info():
    print(f"\t\033[92;1m{'':*^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_1: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_2: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_3: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_4: ^64}\033[0;0m")
    print(f"\t\033[92;1m{'':*^64}\033[0;0m")


def criar_tabela_agendamento(conecxao, sql):
    os.system('cls')
    try:
        conectar = conecxao.cursor()
        conectar.execute(sql)
        print(f"\t\033[97;42;1m{txt_sucesso_agendamento: ^64}\033[0;0m")
    except Error as erro:
        print(f"\t\033[41;97;1m{erro: ^64}\033[0;0m")
    return


def criar_tabela_usuario(conecxao, sql):
    os.system('cls')
    try:
        conectar = conecxao.cursor()
        conectar.execute(sql)
        print(f"\t\033[97;42;1m{txt_sucesso_usuarios: ^64}\033[0;0m")
    except Error as erro:
        print(f"\t\033[41;97;1m{erro: ^64}\033[0;0m")
    return


def menu_data_base():
    os.system('cls')


vsql_1 = """CREATE TABLE TB_AGE(AG_ID INTEGER PRIMARY KEY AUTOINCREMENT,
AG_DIS VARCHAR (3), AG_LAB VARCHAR (30), AG_DAT VARCHAR (10),
AG_HRI VARCHAR (5), AG_HRF VARCHAR (5), AG_RES VARCHAR (30))"""


vsql_2 = """CREATE TABLE TB_USER(USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
USER_NOME VARCHAR (30), USER_LOGIN VARCHAR (10),
USER_PASS VARCHAR (10), USER_ACCESS VARCHAR (5))"""
print(f"\t\033[97;42;1m{txt_op_usuarios: ^64}\033[0;0m")
print(f"\t\033[97;42;1m{txt_op_agendamento: ^64}\033[0;0m")


opcao = 0
while opcao != 3:
    menu_data_base()
    print(f"""\t\033[97;46;1m{txt_menu_principal: ^64}\033[0;0m\n    
\t\033[33;1m{n_op_01: >6}\033[0;0m - \033[97;1m{txt_op_consulta: <55}\033[0;0m
\t\033[33;1m{n_op_02: >6}\033[0;0m - \033[97;1m{txt_op_logar: <55}\033[0;0m\n
\t\033[33;1m{n_op_03: >6}\033[0;0m - \033[97;1m{txt_op_sair: <55}\033[0;0m""")
    info()
    try:
        opcao = int(input(f"\t\033[35;1m{txt_interacao_opcao: >32}\033[0;0m"))
        if opcao == 1:
            criar_tabela_agendamento(vcon, vsql_1)
        elif opcao == 2:
            criar_tabela_usuario(vcon, vsql_2)
        elif opcao == 3:
            vcon.close()
            os.system('cls')
            print(f"\t\033[97;42;1m{txt_sucesso_sair: ^64}\033[0;0m")
            import Sis_Agen_Menu
        else:
            os.system('cls')
            print(f"\t\033[97;43m{txt_sugestao_opc_inv: ^64}\033[0;0m")
            os.system('pause')
    except ValueError:
        os.system('cls')
        print(f"\t\033[97;43m{txt_sugestao_opc_inv: ^64}\033[0;0m")
        os.system('pause')
