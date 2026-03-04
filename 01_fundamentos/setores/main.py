estoque = ('Monitor', 5, 'Informática', 'Teclado', 12, 'Informática', 'Mouse', 0, 'Acessórios')

for pos in range(0, len(estoque), 3):
    alerta = ''
    if estoque[pos + 1] == 0:
        alerta = '[REPOR]'
    
    print(f'{estoque[pos].ljust(20, '.')} {estoque[pos + 1]:<5} Setor: {estoque[pos + 2]} {alerta}')
