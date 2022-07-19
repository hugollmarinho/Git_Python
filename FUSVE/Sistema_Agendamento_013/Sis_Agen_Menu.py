import os


txt_menu_principal = str("SISTEMA DE AGENDAMENTO (V.0.13)")
n_op_01 = int("01")
n_op_02 = int("02")
n_op_03 = int("03")
txt_inf_1 = str("Universidade de Vassouras - Campus Maricá")
txt_inf_2 = str("Desenvolvido pelo aluno de Engenharia de Software")
txt_inf_3 = str("Hugo Marinho - 2022.1 - Turma A")
txt_inf_4 = str("Pensamento Computacional - Alessandra Alves Fonseca Vargas")
txt_op_daba = str("Criar Criar Data Base.")
txt_op_sal = str("Abrir o Sistema de Agendamento .")
txt_op_sair = str("Sair.")
txt_sugestao_opc_inv = str("Opção Invalida.")
txt_sucesso_sair = str("MUITO OBRIGADO POR USAR O SISTEMA DE AGENDAMENTO")
txt_interacao_opcao = str("Digite a Opção Desejada: ")

def menu_data_base():
    os.system('cls')

def info():
    print(f"\t\033[92;1m{'':*^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_1: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_2: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_3: ^64}\033[0;0m")
    print(f"\t\033[92;1m{txt_inf_4: ^64}\033[0;0m")
    print(f"\t\033[92;1m{'':*^64}\033[0;0m")


opcao = 0


while opcao != 3:
    menu_data_base()
    print(f"""\t\033[97;46;1m{txt_menu_principal: ^64}\033[0;0m\n    
\t\033[33;1m{n_op_01: >6}\033[0;0m - \033[97;1m{txt_op_daba: <55}\033[0;0m
\t\033[33;1m{n_op_02: >6}\033[0;0m - \033[97;1m{txt_op_sal: <55}\033[0;0m\n
\t\033[33;1m{n_op_03: >6}\033[0;0m - \033[97;1m{txt_op_sair: <55}\033[0;0m""")
    info()
    try:
        opcao = int(input(f"\t\033[35;1m{txt_interacao_opcao: >32}\033[0;0m"))
        if opcao == 1:
            import Sis_Agen_CDB
        elif opcao == 2:
            import Sis_Agen_Sist
        elif opcao == 3:
            os.system('cls')
            print(f"\t\033[97;42;1m{txt_sucesso_sair: ^64}\033[0;0m")
            exit()
        else:
            os.system('cls')
            print(f"\t\033[97;43m{txt_sugestao_opc_inv: ^64}\033[0;0m")
            os.system('pause')
    except ValueError:
        os.system('cls')
        print(f"\t\033[97;43m{txt_sugestao_opc_inv: ^64}\033[0;0m")
        os.system('pause')