lista_impar = []
lista_par = []
lista = []

while True:
    num_usuario = int(input('Digite um valor: '))
    lista.append(num_usuario)
    
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]

    if opcao == 'N':
        break    

for num in lista:
    if num % 2 == 0: 
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(lista)
print(lista_impar)
print(lista_par)