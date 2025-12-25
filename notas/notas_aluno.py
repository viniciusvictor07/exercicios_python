# Função que calcula a média e a situação do aluno
def situacao_aluno(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    return media, situacao

# Notas 
nota1 = float(input('Digite sua primeira nota aqui: '))
nota2 = float(input('Digite sua segunda nota aqui: '))
nota3 = float(input('Digite sua terceira nota aqui: '))

media, resultado = situacao_aluno(nota1, nota2, nota3)

print(f"Média: {media:.1f}, Situação: {resultado}")