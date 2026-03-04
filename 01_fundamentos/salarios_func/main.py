elenco = {}

for i in range(0,2):
    nome = input(f'Digite o nome do {i+1}º jogador: ').capitalize().strip()
    if nome == "Sair":
        break
    pos = input(f'Digite a posição do {nome}: ')
    sal = float(input(f'Digite o salário do {nome}: '))    
    elenco[nome] = {"posicao": pos, "salario": sal}

def relatorio_financeiro(dados_time):
    maior_s = 0
    maior_j = ""
    soma = 0
    
    for nome, info in dados_time.items():    
        if info["salario"] > maior_s:
            maior_s = info["salario"]
            maior_j = nome 
        soma += info["salario"]

    print('-'*30)
    print('RELÁTORIO FINANCEIRO'.center(30))
    print('-'*30)
    
    print(f'{"JOGADORES":<15} {"POSIÇÃO":<15} {"SALÁRIO":<10}')
    for nome, info in elenco.items():
        print(f'{nome:<15} {info["posicao"].upper():<15} R$ {info["salario"]:<10.2f}'  )

    print()
    print(f'Folha salarial de todos os jogadores: R$ {soma:.2f}')
    print(f'Jogador mais caro: {maior_j} (R$ {maior_s:.2f})')


relatorio_financeiro(elenco)