def linha(txt):
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


def idade_voto(idade):
    if idade < 16:
        situação = "negado"
    elif idade >= 16 and idade < 18:
        situação = "opcional"
    elif idade >= 70:
        situação = "opcional"
    else:
        situação = "obrigatório"
    
    return situação


jogadores = {}

while True:

    jogador_id = int(input('Digite o ID do jogador: '))
    nome = input('Digite o nome do jogador: ')  
    posição = input('Digite a posição do jogador: ') 
    idade = int(input('Digite a idade do jogador: '))
    salário = float(input('Digite o salário do jogador: '))

    jogadores[jogador_id] = {
        "nome": nome,
        "posição": posição,
        "idade": idade,
        "salário": salário
    }
 
    continuar = input("Deseja cadastrar outro jogador? (s/n): ").lower()[0]
    if continuar != 's':
        break


total_salarios = sum(info["salário"] for info in jogadores.values())
média_salarial = total_salarios / len(jogadores) if jogadores else 0
maior_salario = 0
menor_salario = 0
maior_jogador = ""
menor_jogador = ""

for id, info in jogadores.items():
    if info["salário"] > maior_salario:
        maior_salario = info["salário"]
        maior_jogador = info["nome"]
    if info["salário"] < menor_salario or menor_salario == 0:
        menor_salario = info["salário"]
        menor_jogador = info["nome"]

linha("Relatório Financeiro")
print(f"Total gasto em salários: R${total_salarios:.2f}")
print(f"Média salarial do grupo: R${média_salarial:.2f}")
print(f"Jogador mais caro: {maior_jogador} (R${maior_salario:.2f})")
print(f"Jogador mais barato: {menor_jogador} (R${menor_salario:.2f})")

linha("Elenco do Clube")
print(f"{'ID':<5} {'Nome':<15} {'Posição':<10} {'Idade':<5} {'Salário':<10} {'Status Eleitoral':<15}")


for id, info in jogadores.items():
    status = idade_voto(info['idade'])
    print(f"{id:<5} {info['nome']:<15} {info['posição']:<10} {info['idade']:<5} R${info['salário']:<9.2f} {status:<15}")