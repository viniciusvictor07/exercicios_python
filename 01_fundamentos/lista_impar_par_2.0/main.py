lista = [[], []]

for i in range(1,8):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()

print(f'os números pares foram: {lista[0]}')
print(f'os números ímpares foram: {lista[1]}')
print(f'a lista em ordem dos pares e ímpares: {lista}')

