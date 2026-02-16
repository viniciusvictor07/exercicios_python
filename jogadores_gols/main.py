jogadores = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    for c in range(partidas):
        gols.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN': break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N': break

print('-' * 45)
print(f'{"cod":<4} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 45)
for i, j in enumerate(jogadores):
    print(f'{i:<4} {j["nome"]:<15} {str(j["gols"]):<15} {j["total"]:<5}')
print('-' * 45)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}:')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 45)
print('<< VOLTE SEMPRE >>')