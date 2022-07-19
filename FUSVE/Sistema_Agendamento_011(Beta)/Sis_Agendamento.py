import os
import sqlite3
from sqlite3 import Error


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
    os.system("cls")


def consulta_principal():
    os.system("cls")
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
            os.system("pause")
            os.system("cls")
    print("\t\033[35;1mVocê será direcionado para o Menu Principal.\033[0;0m")
    os.system("pause")


def reservar_laboratorio():
    os.system("cls")
    t_reslab = str("RESERVA DE LABORATORIO")
    t_reok = str("RESERVA REALIZADA")
    print(f"\t\033[30;1;46m{t_reslab: ^46}\033[0;0m")
    rl_dis = input("\t\033[35;1mDisponibilidade: \033[0;0m")
    rl_lab = input("\t\033[35;1mInforme o Laboratorio: \033[0;0m")
    rl_dat = input("\t\033[35;1mInforme a Data: \033[0;0m")
    rl_hri = input("\t\033[35;1mInforme a Hora de Inicio: \033[0;0m")
    rl_hrf = input("\t\033[35;1mInforme a Hora Final: \033[0;0m")
    rl_res = input("\t\033[35;1mInforme o Nome da Reserva: \033[0;0m")
    vsql = "INSERT INTO TB_AGE (AG_DIS,AG_LAB, AG_DAT, AG_HRI, AG_HRF, AG_RES) values ('" + rl_dis + "','" + rl_lab + "','" + rl_dat + "','"+rl_hri+"','"+rl_hrf+"','"+rl_res+"')"
    query(vcon, vsql)
    print(f"\t\033[30;43;1m{t_reok: ^46}\033[0:0m")
    os.system("pause")
    os.system("cls")


def cancelar_reserva():
    os.system("cls")
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
    \033[33;1m{"Laboratorio":>15}\033[0;0m {r[2]:<30}
    \033[33;1m{"Disponibilidade:":>15}\033[0;0m {r[1]:<30}
    \033[33;1m{"Reserva:":>15}\033[0;0m {r[6]:<30}
    \033[33;1m{"Data:":>15}\033[0;0m {r[3]:<30}
    \033[33;1m{"Hora Inicial:":>15}\033[0;0m {r[4]:<30}
    \033[33;1m{"Hora Final:":>15}\033[0;0m {r[5]:<30}
    \033[33;1m{"":_^46}\033[0;0m""")
        vcont += 0
        if vcont >= vlim:
            vcont = 0
            os.system("pause")
            os.system("cls")
    conf_can = input("\t\033[35;1mDeseja Deletadar o Registro? \033[0;0m")
    if conf_can == str("SIM"):
        vsqldel="DELETE FROM TB_AGE WHERE AG_ID="+can_id
        query(vcon, vsqldel)
        print(f"\t\033[30;43;1m{t_caok: ^46}\033[0:0m")
    elif conf_can == str("NÃO"):
        print(f"\t\033[30;43;1m{t_canok: ^46}\033[0:0m")
        return menu_acesso()
    else:
        os.system("cls")
        print("t\033[43mOpção Invalida. Digite 'SIM' ou 'NÃO'\033[0;0m")
        os.system("pause")
    os.system("pause")
    os.system("cls")


def consultar_reserva_log():
    os.system("cls")
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
            os.system("pause")
            os.system("cls")
    print("\t\033[35;1mVocê será direcionado para o Menu Principal.\033[0;0m")
    os.system("pause")
    return menu_acesso()


def consultar_usuario():
    os.system("cls")
    t_nuse = str("NOME DE USUARIO:")
    t_loguse = str("LOGIN DO USUARIO:")
    t_accuse = str("TIPO DE ACESSO:")
    t_mconu = str("CONSULTA DE USUARIOS")

    print(f"""\t\033[30;1;46m{t_mconu: ^46}\033[0;0m
\033[33;1m{"":_^46}\033[0;0m""")
    vsql = "SELECT * FROM TB_USER"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"""
    \033[33;1m{t_nuse:>17}\033[0;0m {r[1]:<30}
    \033[33;1m{t_loguse:>17}\033[0;0m {r[2]:<30}
    \033[33;1m{t_accuse:>17}\033[0;0m {r[4]:<30}
    \033[33;1m{"":_^46}\033[0;0m""")
        vcont += 0
        if vcont >= vlim:
            vcont = 0
            os.system("pause")
            os.system("cls")
    print("\t\033[35;1mVocê será direcionado para a Area Administrativa.\033[0;0m")
    os.system("pause")


def cadastrar_usuario():
    os.system("cls")
    t_cadusm = str("CADASTRO DE USUARIOS")
    t_cadok = str("CADASTRO REALIZADO")
    print(f"\t\033[30;1;46m{t_cadusm: ^46}\033[0;0m")
    cd_nome = input("\t\033[35;1mInforme o Nome: \033[0;0m")
    cd_login = input("\t\033[35;1mInforme o Login: \033[0;0m")
    cd_senha = input("\t\033[35;1mInforme a Senha: \033[0;0m")
    cd_acces = input("\t\033[35;1mInforme o Acesso: \033[0;0m")
    vsql = "INSERT INTO TB_USER (user_nome, user_login, user_pass, user_access) values ('"+cd_nome+"', '"+cd_login+"', '"+cd_senha+"', '"+cd_acces+"')"
    query(vcon, vsql)
    print(f"\t\033[30;43;1m{t_cadok: ^46}\033[0:0m")
    os.system("pause")
    os.system("cls")


def menu_acesso():
    t_mac = str("BEM VINDO A AREA ADMINISTRATIVA")
    opaces = 0
    while opaces != 6:
        print(f"\t\033[30;1;46m{t_mac: ^46}\033[0;0m")
        print("""
\t\033[33;1m 1 \033[0;0m- Reservar Laboratorio
\t\033[33;1m 2 \033[0;0m- Consultar Reservas
\t\033[33;1m 3 \033[0;0m- Apagar Reserva
\t\033[33;1m 4 \033[0;0m- Consultar Usuarios
\t\033[33;1m 5 \033[0;0m- Cadastrar Usuarios\n
\t\033[33;1m 6 \033[0;0m- Logoff
\t\033[33;1m 7 \033[0;0m- Sair
        """)
        opaces = int(input("\t\033[35;1mDigite uma Opção: \033[0;0m"))
        if opaces == 1:
            reservar_laboratorio()
        elif opaces == 2:
            consultar_reserva_log()
        elif opaces == 3:
            cancelar_reserva()
        elif opaces == 4:
            consultar_usuario()
        elif opaces == 5:
            cadastrar_usuario()
        elif opaces == 6:
            os.system("cls")
            return menu_principal()
        elif opaces == 7:
            vcon.close()
            os.system("cls")
            print("\t\033[30;43mMuito obrigado por usar o Sistema de Agendamento.\033[0;0m")
            exit()
        else:
            os.system("cls")
            print("\t\t\033[43mOpção Invalida\033[0;0m")
            os.system("pause")


def realizar_login():
    os.system("cls")
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
            os.system("cls")
            print(f"\t\033[30;43;1m{t_uss: ^46}\033[0:0m")
            cpassw = input("\t\033[35;1mDigite o Sua Senha: \033[0;0m")
            if cpassw == rpassw:
                print(f"\t\033[30;43m{t_ses: ^46}\033[0:0m")
                os.system("cls")
                menu_acesso()
            else:
                print(f"\t\033[30;43;1m{t_sen: ^46}\033[0:0m")
                os.system("pause")
                os.system("cls")
                return realizar_login()
        elif clogin == "0":
            os.system("cls")
            return
        else:
            print(f"\t\033[30;43;1m{t_usn: ^46}\033[0:0m")
            print(f"\t\033[30;43m{t_rme: ^46}\033[0;0m")
            return realizar_login()
    except:
        return "SEM ACESSO"


opcao = 0
while opcao != 3:
    menu_principal()
    print("""
\t\033[30;1;46mBEM-VINDO AO SISTEMA DE AGENDAMENTO DOS LABORATÓRIOS\033[0;0m\n
\t\033[33;1m 1 \033[0;0m- Consulta
\t\033[33;1m 2 \033[0;0m- Realizar Login\n
\t\033[33;1m 3 \033[0;0m- Sair\n
\t\033[96;1m___________________________________________________________
\t\033[93;1m       Universidade de Vassouras - Campus Maricá
\t    Desenvolvido pelo aluno de Engenharia de Software
\t            Hugo Marinho - 2022.1 - Turma A
\tPensamento Computacional - Alessandra Alves Fonseca Vargas\033[0;0m
\t\033[96;1m___________________________________________________________\033[0;0m""")
    opcao = int(input("\t\033[35;1mDigite uma Opção: \033[0;0m"))
    if opcao == 1:
        consulta_principal()
    elif opcao == 2:
        realizar_login()
    elif opcao == 3:
        vcon.close()
        os.system("cls")
        print("\t\033[30;43mMuito obrigado por usar o Sistema de Agendamento.\033[0;0m")
        exit()
    else:
        os.system("cls")
        print("t\033[43mOpção Invalida\033[0;0m")
        os.system("pause")
