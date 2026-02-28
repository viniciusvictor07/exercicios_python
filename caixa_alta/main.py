def caixa_alta(nome, caixa_alta=False):
    nome = nome.strip()
    if caixa_alta:
        return nome.upper()
    else:
        return nome.title()


nomes = {}

while True:    
    nome = input('Digite seu nome (ou "sair"): ')
    if nome == 'sair':
        break
    resp = input('Deseja o nome em caixa alta? [S/N] ').upper().strip()
    if resp == 'S':
        nomes[nome] = caixa_alta(nome, caixa_alta=True)
    else:
        nomes[nome] = caixa_alta(nome)

print("\nNomes formatados:")
for original, formatado in nomes.items():
    print(f"{original} -> {formatado}")