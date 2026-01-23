num = []
for i in range(0,5):
    num.append(int(input('Digite um valor: ')))

menor = min(num)
maior = max(num)

print(f'o maior número foi {maior}, o menor {menor}')

for v, i in enumerate(num):
    if i == menor:
        print(f'o menor valor está na {v + 1}ª posição')
    if i == maior:
        print(f'o maior valor está na {v + 1}ª posição')