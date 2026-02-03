pessoas = []
pesado = leve = 0

while True:
    pessoas.append([input('Digite o nome: '), int(input('Digite o peso: '))])
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'N':
        break

# descobrir mais pesado/leve

for i, p in enumerate(pessoas):
    if i == 0:
        pesado = p[1]
        leve = p[1]
    else:
        if p[1] > pesado:
            pesado = p[1]
        if p[1] < leve:
            leve = p[1]

for p in pessoas:
    if p[1] == pesado:
        print(p[0])
    if p[1] == leve:
        print(p[0])

# quantas pessoas

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas. ')

# lista das mais pesadas

print(f'O maior peso foi de {pesado}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == pesado:
        print(f'[{p[0]}] ', end='')

print()

# lista das mais leves

print(f'O menor peso foi de {leve}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'[{p[0]}] ', end='')