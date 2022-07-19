import os
import sqlite3
from sqlite3 import Error


# print("\t\t\033[30;43mMANUTENÇÃO\033[0;0m")


def conecxaobanco():
    caminho = 'Sis_Agendamento.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Operação Realizada com Sucesso")


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res


vcon = conecxaobanco()


def menu_principal():
    os.system("clear||cls")
    print("""
\t\033[30;1;46mBEM-VINDO AO SISTEMA DE AGENDAMENTO DOS LABORATÓRIOS\033[0;0m

\t\033[33;1m 1 \033[0;0m- Consulta
\t\033[33;1m 2 \033[0;0m- Realizar Login

\t\033[33;1m 3 \033[0;0m- Sair

\t\033[96;1m___________________________________________________________
\t\033[93;1m       Universidade de Vassouras - Campus Maricá
\t    Desenvolvido pelo aluno de Engenharia de Software
\t            Hugo Marinho - 2022.1 - Turma A
\tPensamento Computacional - Alessandra Alves Fonseca Vargas\033[0;0m
\t\033[96;1m___________________________________________________________\033[0;0m""")


def menu_consulta():
    os.system("clear||cls")
    t_id = str("Identificador:")
    t_lab = str("Laboratorio:")
    t_dis = str("Disponivel:")
    t_res = str("Reservado:")
    t_dat = str("Data:")
    t_hri = str("Hora Inicial:")
    t_hrf = str("Hora Final:")
    t_esp = str("")
    t_mcon = str("CONSULTA DA AGENDA DOS LABORATÓRIOS")

    print(f"""\t\033[30;1;46m{t_mcon: ^46}\033[0;0m
    \033[33;1m{t_esp:_^46}\033[0;0m""")
    vsql = "SELECT * FROM TB_AGE"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"""
    \033[33;1m{t_id:>15}\033[0;0m {r[0]:<30}
    \033[33;1m{t_lab:>15}\033[0;0m {r[2]:<30}
    \033[33;1m{t_dis:>15}\033[0;0m {r[1]:<30}
    \033[33;1m{t_res:>15}\033[0;0m {r[6]:<30}
    \033[33;1m{t_dat:>15}\033[0;0m {r[3]:<30}
    \033[33;1m{t_hri:>15}\033[0;0m {r[4]:<30}
    \033[33;1m{t_hrf:>15}\033[0;0m {r[5]:<30}
    \033[33;1m{t_esp:_^46}\033[0;0m""")
        vcont += 0
        if vcont >= vlim:
            vcont = 0
            os.system("pause||read")
            os.system("clear||cls")
    print("\t\033[35;1mVocê será direcionado para o Menu Principal.\033[0;0m")
    os.system("pause||read")


def res_lab():
    os.system("clear||cls")
    t_reslab = str("RESERVA DE LABORATORIO")
    t_reok = str("RESERVA REALIZADA")
    print(f"\t\033[30;1;46m{t_reslab: ^46}\033[0;0m")
    rl_dis = input("\t\033[35;1mDigite a Disponibilidade: \033[0;0m")
    rl_lab = input("\t\033[35;1mDigite o Laboratorio: \033[0;0m")
    rl_dat = input("\t\033[35;1mDigite a Data: \033[0;0m")
    rl_hri = input("\t\033[35;1mDigite a Hora Inicial: \033[0;0m")
    rl_hrf = input("\t\033[35;1mDigite a Hora Final: \033[0;0m")
    rl_res = input("\t\033[35;1mDigite o Nome da Reserva: \033[0;0m")
    vsql = "INSERT INTO TB_AGE (AG_DIS,AG_LAB, AG_DAT, AG_HRI, AG_HRF, AG_RES) values ('" + rl_dis + "','" + rl_lab + "','" + rl_dat + "','"+rl_hri+"','"+rl_hrf+"','"+rl_res+"')"
    query(vcon, vsql)
    print(f"\t\033[30;43;1m{t_reok: ^46}\033[0:0m")
    os.system("pause||read")
    os.system("clear||cls")


def can_res():
    os.system("clear||cls")
    t_canr = str("CANCELAMENTO DE RESERVA DE LAB.")
    t_caok = str("CANCELAMENTO REALIZADO")
    t_canok = str("CANCELAMENTO NÃO REALIZADO")
    print(f"\t\033[30;1;46m{t_canr: ^46}\033[0;0m")
    can_id = input("\t\033[35;1mDigite o ID do registro a ser Deletado: \033[0;0m")
    vsql = "SELECT * FROM TB_AGE WHERE AG_ID="+can_id
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"""\033[33;1m{"ID:":>15}\033[0;0m {r[0]:<30}
    \033[33;1m{"Laboratorio"::>15}\033[0;0m {r[2]:<30}
    \033[33;1m{"Disponibilidade:":>15}\033[0;0m {r[1]:<30}
    \033[33;1m{"Reserva:":>15}\033[0;0m {r[6]:<30}
    \033[33;1m{"Data:":>15}\033[0;0m {r[3]:<30}
    \033[33;1m{"Hora Inicial:":>15}\033[0;0m {r[4]:<30}
    \033[33;1m{"Hora Final:":>15}\033[0;0m {r[5]:<30}
    \033[33;1m{"":_^46}\033[0;0m""")
        vcont += 0
        if vcont >= vlim:
            vcont = 0
            os.system("pause||read")
            os.system("clear||cls")
    conf_can = input("\t\033[35;1mDeseja Deletadar o Registro? \033[0;0m")
    if conf_can == str("SIM"):
        vsqldel="DELETE FROM TB_AGE WHERE AG_ID="+can_id
        query(vcon, vsqldel)
        print(f"\t\033[30;43;1m{t_caok: ^46}\033[0:0m")
    elif conf_can == str("NÃO"):
        print(f"\t\033[30;43;1m{t_canok: ^46}\033[0:0m")
        return menu_acesso()
    else:
        os.system("clear||cls")
        print("t\033[43mOpção Invalida. Digite 'SIM' ou 'NÃO'\033[0;0m")
        os.system("pause||read")
    os.system("pause||read")
    os.system("clear||cls")


def log_con():
    os.system("clear||cls")
    vsql = "SELECT * FROM TB_AGE"
    res = consultar(vcon, vsql)
    t_mcon = str("CONSULTA DA AGENDA DOS LABORATÓRIOS")
    vlim=10
    vcom=0

    print(f"""\t\033[30;1;46m{t_mcon: ^46}\033[0;0m
    \033[33;1m{"":_^46}\033[0;0m""")
    for r in res:
        print(f"""\033[33;1m{"ID:":>15}\033[0;0m {r[0]:<30}
    \033[33;1m{"Laboratorio"::>15}\033[0;0m {r[2]:<30}
    \033[33;1m{"Disponibilidade:":>15}\033[0;0m {r[1]:<30}
    \033[33;1m{"Reserva:":>15}\033[0;0m {r[6]:<30}
    \033[33;1m{"Data:":>15}\033[0;0m {r[3]:<30}
    \033[33;1m{"Hora Inicial:":>15}\033[0;0m {r[4]:<30}
    \033[33;1m{"Hora Final:":>15}\033[0;0m {r[5]:<30}""")
        vcom += 0
        if vcom >= vlim:
            vcom = 0
            os.system("pause||read")
            os.system("clear||cls")
    print("\t\033[35;1mVocê será direcionado para o Menu Principal.\033[0;0m")
    os.system("pause||read")
    return menu_acesso()


def con_user():
    print("Consultar Usuarios")


def cad_user():
    print("Cadastrar Usuarios")


def menu_acesso():
    t_mac = str("BEM VINDO A AREA ADMINISTRATIVA")
    opaces = 0
    while opaces != 6:
        print(f"\t\033[30;1;46m{t_mac: ^46}\033[0;0m")
        print("""
            \t\033[33;1m 1 \033[0;0m- Reservar Laboratorio
            \t\033[33;1m 2 \033[0;0m- Consultar Reservas
            \t\033[33;1m 3 \033[0;0m- Cancelar Reserva
            \t\033[33;1m 4 \033[0;0m- Consultar Usuarios
            \t\033[33;1m 5 \033[0;0m- Cadastrar Usuarios

            \t\033[33;1m 6 \033[0;0m- Logoff
            \t\033[33;1m 7 \033[0;0m- Sair
                """)
        opaces = int(input("\t\033[35;1mDigite uma Opção: \033[0;0m"))
        if opaces == 1:
            res_lab()
        elif opaces == 2:
            log_con()
        elif opaces == 3:
            can_res()
        elif opaces == 4:
            con_user()
        elif opaces == 5:
            cad_user()
        elif opaces == 6:
            return
        elif opaces == 7:
            os.system("clear||cls")
            print("\t\033[30;43mMuito obrigado por usar o Sistema de Agendamento.\033[0;0m")
            exit()
        else:
            vcon.close()
            os.system("clear||cls")
            print("\t\t\033[43mOpção Invalida\033[0;0m")
            os.system("pause||read")


def realizar_login():
    os.system("clear||cls")
    t_mrlog = str("INFORME SUAS CREDENCIAIS")
    t_uss = str("BEM VINDO (A)")
    t_usn = str("USUARIO NÃO ENCONTRADO. TENTE NOVAMENTE")
    t_ses = str("SENHA CORRETA")
    t_sen = str("SENHA INCORRETA. FAÇA LOGIN NOVAMENTE")
    t_rme = str("ou digite '0' para voltar")

    print(f"\n\t\033[30;1;46m{t_mrlog: ^46}\033[0;0m\n")
    rlogin = "ADM"
    rpassw = "123"
    try:
        clogin = input("\t\033[35;1mDigite o Seu Login: \033[0;0m")
        if clogin == rlogin:
            os.system("clear||cls")
            print(f"\t\033[30;43;1m{t_uss: ^46}\033[0:0m")
            cpassw = input("\t\033[35;1mDigite o Sua Senha: \033[0;0m")
            if cpassw == rpassw:
                print(f"\t\033[30;43m{t_ses: ^46}\033[0:0m")
                os.system("clear||cls")
                menu_acesso()
            else:
                print(f"\t\033[30;43;1m{t_sen: ^46}\033[0:0m")
                return realizar_login()
        elif clogin == "0":
            os.system("clear||cls")
            return
        else:
            print(f"\t\033[30;43;1m{t_usn: ^46}\033[0:0m")
            print(f"\t\033[30;43m{t_rme: ^46}\033[0;0m")
            return realizar_login()
    except:
        return "SEM ACESSO"


opc = 0
while opc != 3:
    menu_principal()
    opc = int(input("\t\033[35;1mDigite uma Opção: \033[0;0m"))
    if opc == 1:
        menu_consulta()
    elif opc == 2:
        realizar_login()
    elif opc == 3:
        vcon.close()
        os.system("clear||cls")
        print("\t\033[30;43mMuito obrigado por usar o Sistema de Agendamento.\033[0;0m")
        exit()
    else:
        os.system("clear||cls")
        print("t\033[43mOpção Invalida\033[0;0m")
        os.system("pause||read")
