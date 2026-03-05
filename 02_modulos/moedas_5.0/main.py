from utilidades import dado, moeda

preco = dado.leiaPreco('Digite o preço: R$ ')
taxa_a = int(input('Digite a taxa de aumento (%): '))
taxa_r = int(input('Digite a taxa de redução (%): '))
moeda.resumo(preco, taxa_a, taxa_r)