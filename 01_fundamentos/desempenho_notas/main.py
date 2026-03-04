def notas(*n, sit=False):
    resultado = {}
    resultado['total'] = len(n)
    resultado['maior'] = max(n)
    resultado['menor'] = min(n)
    resultado['media'] = sum(n) / len(n)
    
    if sit:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'BOA'
        elif 5 <= resultado['media'] < 7:
            resultado['situacao'] = 'RAZOÁVEL'
        else:
            resultado['situacao'] = 'RUIM'
    
    return resultado

while True:
    notas_lista = []
    no = int(input('Quantas notas deseja inserir? '))
    
    for i in range(1, no + 1):
        nota = float(input(f'Nota {i}: '))
        notas_lista.append(nota)

    sit_input = input('Deseja incluir a situação da turma? [S/N] ').upper().strip()[0]
    
    if sit_input == 'S':
        resultado = notas(*notas_lista, sit=True)
    else:
        resultado = notas(*notas_lista, sit=False)

    resp = input('Deseja continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break

print(f'Notas: {notas_lista} | Total: {resultado["total"]} | Maior: {resultado["maior"]} | Menor: {resultado["menor"]} | Média: {resultado["media"]:.2f}' + (f' | Situação: {resultado["situacao"]}' if "situacao" in resultado else ''))