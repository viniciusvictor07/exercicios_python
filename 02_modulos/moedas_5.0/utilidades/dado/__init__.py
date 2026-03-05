def leiaPreco(msg):
    while True:
        resp = input(msg)
        valor = resp.replace(',', '.').strip()
        
        if valor.isalpha() or valor == '':
            print(f'ERRO: "{resp}" é um preço inválido!')
        
        else:
            return float(valor)