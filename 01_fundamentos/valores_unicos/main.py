num = []

while True: 
    num_usuario = (int(input('Digite um número: ')))
    if num_usuario not in num:
        num.append(num_usuario)
    else:
        print('Valor duplicado, não vai entrar na lista!')
    
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    
    if opcao == 'N':
            break
num.sort()
print(f'Sua lista em ordem é: {num}')