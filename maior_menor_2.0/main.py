pessoas = []

while True:
    temp = []
    temp.append(input('Digite o nome: '))
    temp.append(float(input('Digite o peso: ')))
    
    if len(pessoas) == 0:
            maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]    
    
    pessoas.append(temp[:])    
    temp.clear()
    
    opcao = input('Deseja continuar? [S/N]: ').upper().strip()[0]
    if opcao == 'N':
        break

print(f'{len(pessoas)} pessoas foram cadastradas.')

print(f'O maior peso foi {maior:.2f}Kg. Peso de:', end=' ')
for p in pessoas:
     if p[1] == maior:
          print(p[0])
print(f'O menor peso foi {menor:.2f}Kg. Peso de:', end=' ')
for p in pessoas:
     if p[1] == menor:
          print(p[0])