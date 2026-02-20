def analisar_turma(n):
    media_nota = sum(n) / len(n)
    print(f'a média das notas foi: {media_nota}')
    print(f'a maior nota foi {max(n)}')

notas = []

while True:
    resp = (input('Digite a nota (ou "sair"): ')).upper().strip()
    if resp == "SAIR":
        break
    else:
        nota = float(resp)
        notas.append(nota)

if len(notas) > 0:
    analisar_turma(notas)
else:
    print("Nenhuma nota foi registrada.")