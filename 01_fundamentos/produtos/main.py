produto = None
produto_barato = None
valor_produto = 0
valor_barato = 0 
total_gasto = 0
produto_acima = 0
cont = 0 
# MENU
print('Seja bem-vindo.')
while True: 
    print('='*30)
    print("""Escolha uma das opções a seguir: 
          [ 1 ] Colocar produto
          [ 2 ] Encerrar""")
    opcao = int(input('Digite a sua opção: '))
    
    if opcao == 2:
        break
   
    if opcao == 1:
        produto = input('Digite o nome do produto: ')
        valor_produto = float(input('Agora, digite o valor do produto: '))
        cont += 1
 
   
        # nome do produto mais barato    
        if cont == 1:
            produto_barato = produto 
            valor_barato = valor_produto
        
        elif valor_produto < valor_barato:
            valor_barato = valor_produto
            produto_barato = produto

        # produtos acima de 1000
        if valor_produto > 1000:
            produto_acima += 1
        
        # total gasto
        total_gasto += valor_produto

print(f'O total gasto foi R${total_gasto:.2f}, {produto_acima} estavam acima de R$1.000,00 e o produto mais barato foi {produto_barato}')