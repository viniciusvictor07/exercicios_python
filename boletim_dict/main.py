aluno = {}
aluno['nome'] = input('Digite o nome: ')
aluno['media'] = float(input('Digite a média: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

for k, v in aluno.items():
    print(f'{k}: {v}')