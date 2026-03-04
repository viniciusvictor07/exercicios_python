def pagamento(valor_produto, desconto=0):
    return f'Valor do produto: R${valor_produto:.2f} | Desconto: {desconto}% | Valor final: R${valor_produto * (1 - desconto / 100):.2f}'

while True:
    resp = input('Digite o valor do produto (ou "sair"): ')
    if resp.lower() == 'sair':
        break
    valor_produto = resp

    if valor_produto.isnumeric():
        desconto = input('Digite o desconto (deixe vazio para 0%): ')
        
        if desconto.isnumeric():
            print(pagamento(float(valor_produto), float(desconto)))
        else:
            print(pagamento(float(valor_produto)))
    else:
        print('Valor não informado!')