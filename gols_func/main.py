def analisa_gols(art):
    maior_g = 0

    for j, g in art.items():
        if g > maior_g:
            maior_g = g
            maior_j = j
    
    print(f'Artilheiro do time: {maior_j}, com {maior_g} gols no total')
   

artilharia = {}

for i in range(0,3):
    nome = input('Digite o nome do jogador: ').capitalize().strip()
    nota = int(input('Digite quantos gols: '))
    artilharia[nome] = nota

analisa_gols(artilharia)