
num1 = int(input('Digite o primeiro valor: ').strip())
num2 = int(input('Digite o segundo valor: ').strip())
opcao = 0 

# menu
while opcao != 5:
    print('=-='*10)
    print("""      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa""")
    opcao = int(input('>>>>> Qual a sua opção? ').strip())
    
    # somar
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma de {num1} e {num2} é {soma}')
   
    # multiplicar
    elif opcao == 2: 
        soma = num1 * num2
        print(f'A multiplicação de {num1} vezes {num2} é {soma}')
    
    # maior número
    elif opcao == 3: 
        if num1 > num2:
            maior = num1
            print(f'O maior número é o {maior}.')    
        elif num2 > num1:
            maior = num2
            print(f'O maior número é o {maior}.')
        else: 
            print('Ambos os valores são iguais!')

    # novos números
    elif opcao == 4:
        num1 = int(input('Digite o primeiro valor: ').strip())
        num2 = int(input('Digite o segundo valor: ').strip())
    # sair do programa
    elif opcao == 5:
        print('Saindo...')
    else:    
        print('Opção inválida. Tente novamente: ')
print('Fim!')
