def linha(titulo):
    print('-' * 40)
    print(f'{titulo:^40}')
    print('-' * 40)


def calcular_bonus(salario, nivel):
    if nivel == 1:
        bonus_tipo = "10%"
        bonus_valor = salario * 0.10
    elif nivel == 2:
        bonus_tipo = "20%"
        bonus_valor = salario * 0.20
    elif nivel == 3:
        bonus_tipo = "30%"
        bonus_valor = salario * 0.30
    else:
        bonus_tipo = "Nível inválido"
        bonus_valor = 0
    
    return bonus_tipo, bonus_valor


empresa = {}

while True:
    nome = input('Nome do funcionário (ou "sair"): ')
    if nome == 'sair':
        break
    salario = float(input('Salário do funcionário: '))
    nivel = int(input('Nível do funcionário (1, 2 ou 3): '))
    
    bonus_tipo, bonus_valor = calcular_bonus(salario, nivel)
    
    empresa[nome] = {
        'salario': salario,
        'nivel': nivel,
        'bonus_tipo': bonus_tipo,
        'bonus_valor': bonus_valor,
        'bonus_total': salario + bonus_valor
    }


linha("Relatório de Bônus da Empresa")
print(f"{'Funcionário':<15} {'Nível':<8} {'Salário':<14} {'Bônus Tipo':<15} {'Valor do Bônus':<18} {'Salário total':<14}")

for func, info in empresa.items():
    print(f"{func:<15} {info['nivel']:<8} R${info['salario']:<14.2f} {info['bonus_tipo']:<15} R${info['bonus_valor']:<14.2f} R${info['bonus_total']:<18.2f}")