inv_itens = {}
quantia_itens = []
inv = []

while True:
    inv_itens['item'] = input('Digite o nome do item: ')
    inv_itens['quantia_item'] = int(input('Digite a quantidade: '))

    quantia_itens.append(inv_itens['quantia_item'])
    inv.append(inv_itens.copy())

    resp = input("Deseja continuar? [S/N]: ").upper().strip()
    if resp == 'N':
            break

for p in inv:
    print(f'{p["item"]}: {p["quantia_item"]}')

print(f'{sum(quantia_itens)} itens no total.')