livro = {}
biblioteca = []
livro_grande = []
livro_menor = []

while True:
    livro_nome = input('Digite o nome do livro (ou "sair"): ').upper().strip()
    if livro_nome == "SAIR":
        break

    livro['nome'] = livro_nome
    livro['paginas'] = int(input('Quantas páginas? '))
    
    if livro['paginas'] < 300:
        livro['categoria'] = 'LEITURA RÁPIDA'
        livro_menor.append(livro['nome'])
    
    if livro['paginas'] >= 300:
        livro['categoria'] = 'LIVRÃO'
        livro_grande.append(livro['nome'])

    biblioteca.append(livro.copy())

print(f'{sum(item["paginas"] for item in biblioteca)} páginas no total')
print(f'livros da categoria LIVRÃO: {livro_grande}')
