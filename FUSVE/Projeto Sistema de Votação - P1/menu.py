arq1 = open('votos.txt', 'r')
arq2 = open('candidatos.txt', 'r')

votos = []
candidatos = []

for c in arq1:
    votos = c.split()

for c2 in arq2:
    candidatos.append(c2.split()[1])

for c in range(len(candidatos)):
    print(f'candidato número {candidatos[c]} --> {votos.count(candidatos[c])} votos')