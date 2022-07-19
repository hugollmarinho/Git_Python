import os
import sqlite3
from sqlite3 import Error


txt_menu_adminis = "Área Administrativa"
txt_menu_bv_sal = "Bem-Vindo Ao Sistema de Agendamento dos Laboratórios"
txt_menu_cad_user = "Cadastro de Usuários"
txt_menu_can_rese = "Cancelamento de Reserva"
txt_menu_cons_usuario = "Consulta de Usuários"
txt_menu_principal = "Menu Principal"
txt_menu_sal = " Sistema de Agendamento dos Laboratórios "
txt_menu_reselab = "Reserva de Laboratório"
txt_atencao_canc_rese_nok = "Cancelamento Não Realizado"
txt_consulta = "Consulta"
txt_interacao_id_canc = "Digite o ID do Cancelamento: "
txt_interacao_id_canc_conf = "Confirmar Cancelamento de Reserva? "
txt_interacao_opcao = "Digite a Opção Desejada: "
txt_interacao_red_area_adm = "Você Será Direcionado para a Área Administrativa"
txt_interacao_red_menu_prin = "Você Será Direcionado para o Menu Principal"
txt_sucesso_cad_user = "Cadastro Realizado com Sucesso"
txt_sucesso_can_rese_ok = "Cancelamento Realizado com Sucesso"
txt_sucesso_reali = "Operação Realizada com Sucesso"
txt_sucesso_sair = "Muito Obrigado por usar o Sistema de Agendamento"
txt_sugestao_opc_inv = "Opção Invalida."
txt_manutencao = "Sistema em Manutenção"
txt_op_ap_res = "Apagar Reserva"
txt_op_cad_user = "Cadastrar Usuários"
txt_op_con_user = "Consultar Usuários"
txt_op_consulta = "Consulta."
txt_op_data = "Data"
txt_op_data_pd = "Data: (01/07/2022): "
txt_op_disp = "Disponibilidade"
txt_op_disp_pd = "Disponibilidade (SIM ou NÃO): "
txt_op_h_fin = "Hora Final"
txt_op_h_fin_pd = "Hora Final (16:00): "
txt_op_h_ini = "Hora Inicial"
txt_op_h_ini_pd = "Hora Inicial (15:00): "
txt_op_id = "ID"
txt_op_lab = "Laboratório"
txt_op_lab_pd = "Laboratório (ex.: LAB-INF-01): "
txt_op_logar = "Logar."
txt_op_logoof = "Logoof"
txt_op_res_lab = "Reservar Laboratório"
txt_op_rese = "Nome da Reserva"
txt_op_rese_pd = "Nome da reserva: "
txt_op_sair = "Sair."
txt_op_us_acesso = "Tipo de Acesso: "
txt_op_us_login = "Login do Usuário: "
txt_op_us_nome = "Nome do Usuário: "
txt_op_us_senha = "Senha: "
n_op_01 = "01"
n_op_02 = "02"
n_op_03 = "03"
n_op_04 = "04"
n_op_05 = "05"
n_op_06 = "06"
n_op_07 = "07"
txt_inf_01 = "Universidade de Vassouras - Campus Maricá"
txt_inf_02 = "Desenvolvido pelo aluno de Engenharia de Software"
txt_inf_03 = "Hugo Marinho - 2022.1 - Turma A"
txt_inf_04 = "Pensamento Computacional - Alessandra Alves Fonseca Vargas"


def conecta_banco():
    local = "SIS_BETA.db"
    conec = None
    try:
        conec = sqlite3.connect(local)
    except Error as erro:
        print(f"\t\033[41;97;1m{erro: ^64}\033[0;0m")
    return conec


def query(conecxao, sql):
    try:
        conectar = conecxao.cursor()
        conectar.execute(sql)
        conecxao.commit()
    except Error as erro:
        print(f"\t\033[41;97;1m{erro: ^64}\033[0;0m")
    finally:
        print(f"\t\033[97;42;1m{txt_sucesso_reali: ^64}\033[0;0m")


def consultar_banco(conecxao, sql):
    conectar = conecxao.cursor()
    conectar.execute(sql)
    resultado = conectar.fetchall()
    return resultado


vcon = conecta_banco()


def menu_principal():
    os.system('cls')


def manutencao():
    os.system('cls')
    print(f"\t\033[41;97;1m{'': ^64}\033[0;0m")
    print(f"\t\033[41;97;1m{txt_manutencao: ^64}\033[0;0m")
    print(f"\t\033[41;97;1m{'': ^64}\033[0;0m")
    info()
    os.system('pause')


def info():
    print(f"\t\033[92;1m{'':*^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_01: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_02: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_03: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_04: ^64}\033[0;0m")
    print(f"\t\033[92;1m{'':*^64}\033[0;0m")


def reserva_laboratorio():
    os.system('cls')
    print(f"\t\033[41;97;1m{txt_menu_reselab: ^64}\033[0;0m")
    rlab_disp = input(f"\t\033[35;1m{txt_op_disp_pd: >32}\033[0;0m")
    rlab_lab = input(f"\t\033[35;1m{txt_op_lab_pd: >32}\033[0;0m")
    rlab_data = input(f"\t\033[35;1m{txt_op_data_pd: >32}\033[0;0m")
    rlab_h_ini = input(f"\t\033[35;1m{txt_op_h_ini_pd: >32}\033[0;0m")
    rlab_h_fin = input(f"\t\033[35;1m{txt_op_h_fin_pd: >32}\033[0;0m")
    rlab_rese = input(f"\t\033[35;1m{txt_op_rese_pd: >32}\033[0;0m")
    vsql = "INSERT INTO TB_AGE (AG_DIS,AG_LAB, AG_DAT, AG_HRI, AG_HRF, AG_RES) values ('" + rlab_disp + "','" + rlab_lab + "','" + rlab_data + "','" + rlab_h_ini + "','" + rlab_h_fin + "','" + rlab_rese + "')"
    query(vcon, vsql)
    print(f"\t\033[97;42;1m{txt_sucesso_reali: ^64}\033[0;0m")
    os.system("pause")
    os.system("cls")
    area_adminstrativa()


def cancelar_reservas():
    os.system('cls')
    print(f"\t\033[97;46;1m{txt_menu_can_rese: ^64}\033[0;0m")
    canc_id = input(f"\t\033[35;1m{txt_interacao_id_canc: >32}\033[0;0m")
    vsql = "SELECT * FROM TB_AGE WHERE AG_ID=" + canc_id
    res = consultar_banco(vcon, vsql)
    vlimcr = 10
    vcontcr = 0
    for r in res:
        print(f"\t\033[33;1m{txt_op_id: >28}\033[0;0m - \033[97;1m{r[0]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_lab: >28}\033[0;0m - \033[97;1m{r[2]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_disp: >28}\033[0;0m - \033[97;1m{r[1]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_rese: >28}\033[0;0m - \033[97;1m{r[6]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_data: >28}\033[0;0m - \033[97;1m{r[3]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_h_ini: >28}\033[0;0m - \033[97;1m{r[4]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_h_fin: >28}\033[0;0m - \033[97;1m{r[5]: <33}\033[0;0m")
        print(f"\t\033[97;1m{'':-<64}\033[0;0m")
        vcontcr += 0
        if vcontcr >= vlimcr:
            vcontcr = 0
            os.system("pause")
            os.system("cls")
    canc_id_conf = input(f"\t\033[35;1m{txt_interacao_id_canc_conf: >32}\033[0;0m")
    if canc_id_conf == str("SIM"):
        vsql = "DELETE FROM TB_AGE WHERE AG_ID=" + canc_id
        query(vcon, vsql)
        print(f"\t\033[97;42;1m{txt_sucesso_can_rese_ok: ^64}\033[0;0m")
    elif canc_id_conf == str("NÃO"):
        print(f"\t\033[43;97;1m{txt_atencao_canc_rese_nok: ^64}\033[0;0m")
    else:
        os.system("cls")
        print(f"\t\033[97;43m{txt_sugestao_opc_inv: ^64}\033[0;0m")
        os.system("pause")
    print(f"\t\033[35;1m{txt_interacao_red_area_adm: >32}\033[0;0m")
    os.system("pause")
    return area_adminstrativa()


def consulta_reserva_logado():
    os.system('cls')
    print(f"\t\033[97;46;1m{txt_consulta: ^64}\033[0;0m")
    print(f"\t\033[97;1m{'':-<64}\033[0;0m")
    vsql = 'SELECT * FROM TB_AGE'
    con_pri = consultar_banco(vcon, vsql)
    vlin = 10
    vcont = 0
    for r in con_pri:
        print(f"\t\033[33;1m{txt_op_id: >28}\033[0;0m - \033[97;1m{r[0]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_lab: >28}\033[0;0m - \033[97;1m{r[2]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_disp: >28}\033[0;0m - \033[97;1m{r[1]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_rese: >28}\033[0;0m - \033[97;1m{r[6]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_data: >28}\033[0;0m - \033[97;1m{r[3]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_h_ini: >28}\033[0;0m - \033[97;1m{r[4]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_h_fin: >28}\033[0;0m - \033[97;1m{r[5]: <33}\033[0;0m")
        print(f"\t\033[97;1m{'':-<64}\033[0;0m")
        vcont += 0
        if vcont >= vlin:
            vcont = 0
            os.system("pause")
            os.system("cls")
    print(f"\t\033[35;1m{txt_interacao_red_area_adm: ^64}\033[0;0m")
    os.system("pause")
    return area_adminstrativa()


def consultar_usuarios():
    os.system('cls')
    print(f"\t\033[97;46;1m{txt_menu_cons_usuario: ^64}\033[0;0m")
    print(f"\t\033[97;1m{'':-<64}\033[0;0m")
    vsql = "SELECT * FROM TB_USER"
    res = consultar_banco(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print(f"\t\033[33;1m{txt_op_us_nome: >28}\033[0;0m - \033[97;1m{r[1]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_us_login: >28}\033[0;0m - \033[97;1m{r[2]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_us_acesso: >28}\033[0;0m - \033[97;1m{r[4]: <33}\033[0;0m")
        print(f"\t\033[97;1m{'':-<64}\033[0;0m")
        vcont += 0
        if vcont >= vlim:
            vcont = 0
            os.system("pause")
            os.system("cls")
    print(f"\t\033[35;1m{txt_interacao_red_area_adm: ^64}\033[0;0m")
    os.system("pause")
    return area_adminstrativa()


def cadastro_usuario():
    os.system('cls')
    print(f"\t\033[97;46;1m{txt_menu_cad_user: ^64}\033[0;0m")
    cad_nome = input(f"\t\033[35;1m{txt_op_us_nome: >28}\033[0;0m")
    cad_login = input(f"\t\033[35;1m{txt_op_us_login: >28}\033[0;0m")
    cad_senha = input(f"\t\033[35;1m{txt_op_us_senha: >28}\033[0;0m")
    cad_acces = input(f"\t\033[35;1m{txt_op_us_acesso: >28}\033[0;0m")
    vsql = "INSERT INTO TB_USER (user_nome, user_login, user_pass, user_access) values ('" + cad_nome + "', '" + cad_login + "', '" + cad_senha + "', '" + cad_acces + "')"
    query(vcon, vsql)
    print(f"\t\033[97;42;1m{txt_sucesso_cad_user: ^64}\033[0;0m")
    os.system("pause")
    return area_adminstrativa()


def area_adminstrativa():
    os.system('cls')
    opcadm = 0
    while opcadm != 8:
        print(f"\t\033[97;46;1m{txt_menu_sal: ^64}\033[0;0m")
        print(f"\t\033[97;46;1m{txt_menu_adminis: ^64}\033[0;0m\n")
        print(f"\t\033[33;1m{n_op_01: >6}\033[0;0m - \033[97;1m{txt_op_res_lab: <55}\033[0;0m")
        print(f"\t\033[33;1m{n_op_02: >6}\033[0;0m - \033[97;1m{txt_op_consulta: <55}\033[0;0m")
        print(f"\t\033[33;1m{n_op_03: >6}\033[0;0m - \033[97;1m{txt_op_ap_res: <55}\033[0;0m")
        print(f"\t\033[33;1m{n_op_04: >6}\033[0;0m - \033[97;1m{txt_op_con_user: <55}\033[0;0m")
        print(f"\t\033[33;1m{n_op_05: >6}\033[0;0m - \033[97;1m{txt_op_cad_user: <55}\033[0;0m\n")
        print(f"\t\033[33;1m{n_op_06: >6}\033[0;0m - \033[97;1m{txt_op_logoof: <55}\033[0;0m")
        print(f"\t\033[33;1m{n_op_07: >6}\033[0;0m - \033[97;1m{txt_op_sair: <55}\033[0;0m")
        try:
            opcadm = int(input(f"\t\033[35;1m{txt_interacao_opcao: >32}\033[0;0m"))
            if opcadm == 1:
                reserva_laboratorio()
            elif opcadm == 2:
                consulta_reserva_logado()
            elif opcadm == 3:
                cancelar_reservas()
            elif opcadm == 4:
                consultar_usuarios()
            elif opcadm == 5:
                cadastro_usuario()
            elif opcadm == 6:
                menu_principal()
            elif opcadm == 7:
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


def login():
    txt_menu_login = "LOGIN".upper()
    txt_interacao_login = "Digite seu Login: "
    txt_interacao_senha = "Digite sua Senha: "
    txt_atencao_valida = "Erro ao Validar os Dados de Login"
    txt_erro_senha = "Senha Incorreta"
    os.system('cls')
    print(f"\t\033[97;46;1m{txt_menu_login: ^64}\033[0;0m\n")
    nome_usuario = input(f"\t\033[35;1m{txt_interacao_login: >32}\033[0;0m")
    senha = input(f"\t\033[35;1m{txt_interacao_senha: >32}\033[0;0m")

    banco = sqlite3.connect("SIS_BETA.db")
    cursor = banco.cursor()
    cursor.execute("SELECT USER_PASS FROM TB_USER WHERE USER_LOGIN ='{}'".format(nome_usuario))
    senha_db = cursor.fetchall()
    print(senha_db[0][0])

    banco.close()

    if senha == senha_db[0][0]:
        area_adminstrativa()
    elif senha != senha_db[0][0]:
        print(f"\t\033[41;97;1m{txt_erro_senha: ^64}\033[0;0m")
        os.system("pause")
        return login()
    else:
        print(f"\t\033[43;97;1m{txt_atencao_valida: ^64}\033[0;0m")
        os.system("pause")
        return menu_principal()


def consulta_princ():
    os.system('cls')
    print(f"\t\033[97;46;1m{txt_menu_sal: ^64}\033[0;0m")
    print(f"\t\033[97;46;1m{txt_consulta: ^64}\033[0;0m")
    print(f"\t\033[97;1m{'':-<64}\033[0;0m")
    vsql = 'SELECT * FROM TB_AGE'
    con_pri = consultar_banco(vcon, vsql)
    vlin = 10
    vcont = 0
    for r in con_pri:
        print(f"\t\033[33;1m{txt_op_id: >28}\033[0;0m - \033[97;1m{r[0]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_lab: >28}\033[0;0m - \033[97;1m{r[2]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_disp: >28}\033[0;0m - \033[97;1m{r[1]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_rese: >28}\033[0;0m - \033[97;1m{r[6]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_data: >28}\033[0;0m - \033[97;1m{r[3]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_h_ini: >28}\033[0;0m - \033[97;1m{r[4]: <33}\033[0;0m")
        print(f"\t\033[33;1m{txt_op_h_fin: >28}\033[0;0m - \033[97;1m{r[5]: <33}\033[0;0m")
        print(f"\t\033[97;1m{'':-<64}\033[0;0m")
        vcont += 0
        if vcont >= vlin:
            vcont = 0
            os.system("pause")
            os.system("cls")
    print(f"\t\033[35;1m{txt_interacao_red_menu_prin: ^64}\033[0;0m")
    os.system("pause")


opcao = 0
while opcao != 3:
    menu_principal()
    print(f"""\t\033[97;46;1m{txt_menu_bv_sal: ^64}\033[0;0m
\t\033[97;46;1m{txt_menu_principal: ^64}\033[0;0m\n    
\t\033[33;1m{n_op_01: >6}\033[0;0m - \033[97;1m{txt_op_consulta: <55}\033[0;0m
\t\033[33;1m{n_op_02: >6}\033[0;0m - \033[97;1m{txt_op_logar: <55}\033[0;0m\n
\t\033[33;1m{n_op_03: >6}\033[0;0m - \033[97;1m{txt_op_sair: <55}\033[0;0m""")
    info()
    try:
        opcao = int(input(f"\t\033[35;1m{txt_interacao_opcao: >32}\033[0;0m"))
        if opcao == 1:
            consulta_princ()
        elif opcao == 2:
            login()
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
