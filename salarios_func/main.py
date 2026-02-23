def relatorio_financeiro(dados_time):
    total_folha = 0
    maior_salario = 0
    cara_do_time = ""

    print("-" * 30)
    print("RELATÓRIO GERAL DO ELENCO")
    print("-" * 30)

    for nome, info in dados_time.items():
        posicao = info['posicao']
        salario = info['salario']
        
        print(f"Nome: {nome} | Posição: {posicao} | Salário: R${salario:.2f}")

        total_folha += salario

        if salario > maior_salario:
            maior_salario = salario
            cara_do_time = nome

    print("-" * 30)
    print(f"Folha Salarial Total: R${total_folha:.2f}")
    print(f"Jogador mais caro: {cara_do_time} (R${maior_salario:.2f})")
    print("-" * 30)

elenco = {}

for i in range(0, 2):
    nome_j = input(f"Nome do {i+1}º jogador: ").strip().upper()
    pos_j = input(f"Posição de {nome_j}: ").strip().upper()
    sal_j = float(input(f"Salário de {nome_j}: "))
    
    elenco[nome_j] = {'posicao': pos_j, 'salario': sal_j}

relatorio_financeiro(elenco)