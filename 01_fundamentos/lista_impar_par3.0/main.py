def ParImpar(lista):
    lista_par = []
    lista_impar = []
    
    for num in lista:
        if num % 2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)
    return lista_par, lista_impar


numeros = []

resp = int(input('Quantos números deseja inserir? '))

for i in range(1, resp + 1):
    num = int(input(f'Digite o {i}º número: '))
    numeros.append(num)

pares, impares = ParImpar(numeros)
numeros.sort()

print(f"""Os números pares são: {pares}
Os números ímpares são: {impares}
Lista completa: {numeros}""")
