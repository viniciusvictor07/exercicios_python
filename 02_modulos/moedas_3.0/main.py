from utilidades import moedas
preco = float(input('Digite o preço: R$ '))
print(f"A metade de {moedas.formatar(preco)} é {moedas.metade(preco, True)}")
print(f"O dobro de {moedas.formatar(preco)} é {moedas.dobro(preco, True)}")
print(f"Aumentando 10%, temos {moedas.aumentar(preco, True)}")
print(f"Diminuindo 13%, temos {moedas.diminuir(preco, True)}")