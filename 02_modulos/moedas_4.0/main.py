from utilidades import moedas
preco = float(input('Digite o preço: R$ '))
taxa_a = int(input('Digite a taxa de aumento (%): '))
taxa_r = int(input('Digite a taxa de redução (%): '))

moedas.resumo(preco, taxa_a, taxa_r)