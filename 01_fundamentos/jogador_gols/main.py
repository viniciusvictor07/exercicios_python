jogador = {}
jogador['nome'] = input('Digite o nome do jogador: ')
jogador['partidas'] = int(input('Digite quantas partidas jogadas: '))
gols_partidas = []

for i in range(0, jogador['partidas']):
    gols = int(input(f'Quantos gols na {i+1}ª partida? '))
    gols_partidas.append(gols)

jogador['gols'] = gols_partidas[:]
jogador['gols_total'] = sum(gols_partidas)

print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for p, g in enumerate(jogador['gols']):
    print(f'Na {p+1}ª partida o jogador fez {g} gol(s)')

print(f'Total de {jogador["gols_total"]} gols.')