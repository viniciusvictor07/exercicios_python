alunos = int(input('Digite quantos alunos serão avaliados: '))

# informações do aluno
maior_nota = None
maior_aluno = None
soma_notas = 0
aprovados = 0 
reprovados = 0 

for i in range(1, alunos + 1):
    
    nome = (input('Digite seu nome: '))
    nota_final = int(input('Digite sua nota final: '))
    faltas = int(input('Digite suas faltas: '))

    # aluno com a maior nota
    if maior_nota == None:
        maior_nota = nota_final
        maior_aluno = nome
    elif nota_final > maior_nota:
        maior_nota = nota_final
        maior_aluno = nome

    # quantos alunos foram aprovados
    if nota_final >= 70 and faltas <= 5:
        aprovados += 1
    # quantos alunos foram reprovados
    elif nota_final < 50 or faltas > 10:
        reprovados += 1
    soma_notas += nota_final
# resultados
media = soma_notas / alunos
print(f'a média da turma é de {media:.1f} pontos')
print(f'o aluno com a maior nota foi {maior_aluno}')
print(f'{aprovados} alunos foram aprovados')
print(f'{reprovados} alunos foram reprovados')