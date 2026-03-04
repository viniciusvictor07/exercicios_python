from utilidades import moedas
preco = float(input('Digite o preço: R$ '))
print(f'A metade de {preco} é R$ {moedas.metade(preco)}') 
print(f'O dobro de {preco} é R$ {moedas.dobro(preco)}')
print(f'Aumentando 10%, temos R$ {moedas.aumentar(preco)}') 
print(f'Diminuindo 13%, temos R$ {moedas.diminuir(preco)}')