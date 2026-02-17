fabrica = []
peca = {}
peca_reprov = []
while True:
    nome = input('Digite o nome da peça (ou "sair"): ').upper().strip()
    if nome == "SAIR":
        break
    
    peca['nome'] = nome
    peca['peso'] = float(input('Digite o peso da peça: '))    
    
    if peca['peso'] < 50:
        peca['status'] = "REPROVADO"
    
    if peca['peso'] > 50:
        peca['status'] = "APROVADO"

    fabrica.append(peca.copy())
    
for p in fabrica:
    if p['status'] == "REPROVADO":
        peca_reprov.append(p['nome'])

print(f'peças que foram reprovadas: {peca_reprov}')
