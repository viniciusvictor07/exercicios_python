from datetime import datetime

dados = {}

dados['nome'] = input('Digite seu nome: ')
nasc = int(input('Digite sua data de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se nao tiver): '))
if dados['ctps'] != 0:
    dados['ano_de_contrato'] = int(input('Digite seu ano de contrato: '))
    dados['salario'] = float(input('Digite seu salário: '))
    dados['idade_de_aposento'] = (dados['ano_de_contrato'] + 35) - nasc

for k, v in dados.items():
    print(f'{k.upper()}: {v}')