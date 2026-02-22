def avalia_time(t):
    soma = 0
    for j, n in t.items():
        if n >= 7:
            destaques.append(j)
        soma += n
    media = soma / len(t)

    print(f'Jogadores destaques: {destaques}')
    print(f'Nota média do time: {media}')

time = {}
destaques = []

for j in range(0,5):
    nome_j = input(f'Digite o nome do {j+1}ª jogador: ').upper().strip()
    nota_j = float(input('Digite a nota do jogador: '))
    time[nome_j] = nota_j

avalia_time(time)