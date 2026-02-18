carteira = []
conta = {}
maior_gasto = maior_nome = 0

while True: 
    gasto = input('Digite o nome da conta (ou "sair"): ').upper().strip()
    if gasto == "SAIR":
        break
    conta['conta'] = gasto
    conta['valor'] = float(input('Digite o valor gasto: '))
    
    if conta['valor'] > maior_gasto:
        maior_gasto = conta['valor']
        maior_nome = conta['conta']

    carteira.append(conta.copy())

print(f'Valor total gasto: R${sum(item["valor"] for item in carteira)}')
print(f'A conta mais cara foi: {maior_nome}, custando R${maior_gasto:.2f}')
