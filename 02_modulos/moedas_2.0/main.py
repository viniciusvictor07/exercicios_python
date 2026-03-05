from utilidades import moedas
preco = float(input('Digite o preço: R$ '))
print(f"A metade de {moedas.formatar(preco)} é {moedas.formatar(moedas.metade(preco))}")
print(f"O dobro de {moedas.formatar(preco)} é {moedas.formatar(moedas.dobro(preco))}")
print(f"Aumentando 10%, temos {moedas.formatar(moedas.aumentar(preco))}")
print(f"Diminuindo 13%, temos {moedas.formatar(moedas.diminuir(preco))}")