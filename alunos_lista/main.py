ficha = []

while True: 
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    
    resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break

for i, aluno in enumerate(ficha):
    print(f'{i + 1}º ALUNO: {aluno[0]}, MÉDIA: {aluno[2]}')

while True:
    opc = int(input('Deseja ver a nota de qual aluno? (999 interompe) '))
    if opc == 999:
        break
    if opc <= len(ficha):
        print(f'As notas do aluno {ficha[opc-1][0]} são {ficha[opc-1][1]}')
    else:
        print('Aluno não encontrado!')

    resp = input('Quer continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break