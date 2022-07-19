import sqlite3
from sqlite3 import Error


def conecxao_banco():
    caminho = "Sis_Agendamento.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print("\t\033[1;31m", ex, "\033[0;0m\n")
    return con


vcon = conecxao_banco()


vsql_1 = """
CREATE TABLE TB_AGE(
AG_ID INTEGER PRIMARY KEY AUTOINCREMENT,
AG_DIS VARCHAR (3),
AG_LAB VARCHAR (30),
AG_DAT VARCHAR (10),
AG_HRI VARCHAR (5),
AG_HRF VARCHAR (5),
AG_RES VARCHAR (30))"""
print("\t\033[30;106;1mTabela Agendamento\033[0;0m")


def criar_tabela_1(conecxao, sql):
    try:
        c = conecxao.cursor()
        c.execute(sql)
        print("\t\033[30;42mTabela Criada\033[0;0m\n")
    except Error as ex:
        print("\t\033[1;31m", ex, "\033[0;0m\n")


criar_tabela_1(vcon, vsql_1)


vsql_2 = """
CREATE TABLE TB_USER(
USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
USER_NOME VARCHAR (30),
USER_LOGIN VARCHAR (10),
USER_PASS VARCHAR (10),
USER_ACCESS VARCHAR (5))"""
print("\t\033[30;106;1mTabela Usuarios\033[0;0m")


def criar_tabela_2(conecxao, sql):
    try:
        c = conecxao.cursor()
        c.execute(sql)
        print("\t\033[30;42mTabela Criada\033[0;0m\n")
    except Error as ex:
        print("\t\033[1;31m", ex, "\033[0;0m\n")


criar_tabela_2(vcon, vsql_2)

print("""\t\033[96;1m___________________________________________________________
\t\033[93;1m       Universidade de Vassouras - Campus Maricá
\t    Desenvolvido pelo aluno de Engenharia de Software
\t            Hugo Marinho - 2022.1 - Turma A
\tPensamento Computacional - Alessandra Alves Fonseca Vargas\033[0;0m
\t\033[96;1m___________________________________________________________\033[0;0m""")
vcon.close()
