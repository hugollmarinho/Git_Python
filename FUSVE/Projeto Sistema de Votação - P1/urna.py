print('''
 _____________________
|  _________________  |
| | Urna Eletrônica | |
| |    A G H P Q    | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | |del| |
| |___|___|___| |___| |
| | 4 | 5 | 6 | |con| |
| |___|___|___| |___| |
| | 1 | 2 | 3 | |nul| |
| |___|___|___| |___| |
| | . | 0 | = |       |
| |___|___|___|       |
|_____________________|
''')

try:
    arq = open('candidatos.txt', 'r')

except:
    print('Cadastre algum candidato')
    exit()

votos = open('votos.txt', 'a')

candidatos = []
numeros = []

for c in arq:
    candidatos.append(c.split()[0])
    numeros.append(int(c.split()[1]))

mat = open('eleitores.txt', 'r')

for e in mat:
    matricula = e.split()

print('\n### Candidatos ###')
print('Digite 999 para sair\n\n')

for c in range(0, len(numeros)):
    print(f'{candidatos[c]} - {numeros[c]}')

while True:
    nome = input('Digite seu nome: ')
    if nome == '999': exit()
    mat = input('Digite sua matricula: ')
    if mat == '999': exit()
    open('eleitores.txt', 'r')
    if mat not in matricula or nome not in matricula:
        print('dados inválidos')

    else:
        cand = int(input('\nDigite o número do candidato: '))
        if cand == 999:
            exit()
        if cand not in numeros:
            print('número inválido')
        else:
            votos.write(f'{cand} ')