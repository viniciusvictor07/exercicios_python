def Linha(txt):
    print('-' * 30)
    print(txt.center(30))
    print('-' * 30)


def convocação(elenco):
    soma = 0
    artilharia = []
    garcom_nome = ''
    garcom_assist = 0


    for j in elenco:
        if j['gols'] > 10:
            artilharia.append(j['nome'])

        if j['assist'] > garcom_assist:
            garcom_nome = j['nome']
            garcom_assist = j['assist']

        soma += j['gols']

    return artilharia, garcom_nome, garcom_assist, soma
    

elenco = []

while True:
    nome = input('Digite o nome do jogador: ')
    gols = int(input('Digite o número de gols: '))
    assist = int(input('Digite o número de assistências: '))

    jogador = {
        'nome': nome,
        'gols': gols,
        'assist': assist
    }

    elenco.append(jogador.copy())

    resp = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break

artilharia, garcom_nome, garcom_assist, soma = convocação(elenco)

Linha("ELENCO CONVOCADO")
for j in elenco:
    print(f"Nome: {j['nome']:<15} | Gols: {j['gols']:^5} | Assistências: {j['assist']:>3}")

Linha("RESULTADOS")
print(f"""Jogadores com mais de 10 gols: {artilharia}
Garçom do campeonato: {garcom_nome} com {garcom_assist} assistências
Total de gols do elenco: {soma}""")
