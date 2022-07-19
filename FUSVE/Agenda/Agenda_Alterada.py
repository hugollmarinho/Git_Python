# Universidade de Vassouras - Campus Maricá
# Alessandra Alves Fonseca Vargas
# Pensamento Computacional
# 2022.1 - Turma A
# Hugo Lelly de Lima Marinho
# 202211182

agenda_telefonica = []


def f_nome():
    return input("Nome: ")


def f_telefone():
    return input("Telefone: ")


def f_email():
    return input("E-mail: ")


def f_arquivo():
    return input("Nome da Agenda Telefonica: ")


def f_exibir(nome, telefone, email):
    print("""
    Nome: %s
    Telefone: %s
    E-mail: %s""" % (nome, telefone, email))


def f_novo():
    global agenda_telefonica
    nome = f_nome()
    telefone = f_telefone()
    email = f_email()
    agenda_telefonica.append([nome, telefone, email])


def f_pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda_telefonica):
        if e[0].lower() == mnome:
            return p
    return nome


def f_editar():
    p = f_pesquisa(f_nome())
    if p != None:
        nome = agenda_telefonica[p][0]
        telefone = agenda_telefonica[p][1]
        email = agenda_telefonica[p][2]
        print("Contato Localizado: ")
        f_exibir(nome, telefone, email)
        nome = f_nome()
        telefone = f_telefone()
        email = f_email()
    else:
        print("Contato não encontrado:")


def f_apagar():
    global agenda_telefonica
    nome = f_pesquisa()
    p = f_pesquisa(nome)
    if p != nome:
        del agenda_telefonica[p]
    else:
        print("Contato não encontrado:")


def f_lista():
    print("\nAgenda Telefonica\n\n-----------------")
    for e in agenda_telefonica:
        f_exibir(e[0], e[1], e[2])
    print("-----------------\n")


def f_importar():
    global agenda_telefonica
    nome_arquivo = f_arquivo()
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda_telefonica = []
    for l in arquivo.readlines():
        nome, telefone, email = l.strip().split("#")
        agenda_telefonica.append([nome, telefone, email])
    arquivo.close()


def f_exportar():
    nome_arquivo = f_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda_telefonica:
        arquivo.write("%s#%s#%s\n" % (e[0], e[1], e[2]))
    arquivo.close()


def f_validar(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return (valor)
        except ValueError:
            print("""
            Opção Inválida!
            Escolha uma das opções entre %d e %d.""" % (inicio, fim))


def f_menu():
    print("""
    1 - Novo Contato.
    2 - Editar Contato.
    3 - Apagar Contato.
    4 - Exibir Contatos.
    5 - Exportar Agenda.
    6 - Importar Agenda.

    0 - Sair.
    """)
    return f_validar("Escolha uma opção: ", 0, 6)


while True:
    escolha = f_menu()
    if escolha == 0:
        break
    if escolha == 1:
        f_novo()
    if escolha == 2:
        f_editar()
    if escolha == 3:
        f_apagar()
    if escolha == 4:
        f_exibir()
    if escolha == 5:
        f_exportar()
    if escolha == 6:
        f_importar()