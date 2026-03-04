lista = []

while True:
    num_usuario = int(input('Digite um valor: '))
    lista.append(num_usuario)
    
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]

    if opcao == 'N':
        break    

print(f'{len(lista)} números foram digitados')

lista.sort(reverse=True)
print(f'a ordem decrescente dos números é {lista}')

# se o valor 5 está na lista 
if 5 in lista:
    print('O valor 5 foi digitado e está na lista')
else:   
    print('O valor 5 não foi digitado e não está na lista')