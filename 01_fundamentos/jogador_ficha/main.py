def ficha(nome='desconhecido', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

nome = input('Nome do jogador: ')
gols = input('Número de gols: ')

if nome == '':
    if gols.isnumeric():
        print(ficha(gols=int(gols)))
    else:
        print(ficha())
else:
    if gols.isnumeric():
        print(ficha(nome, int(gols)))
    else:
        print(ficha(nome))