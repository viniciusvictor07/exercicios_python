from random import randint

def sorteia(l):
    for i in range(0,5):
        num = randint(1,10)
        l.append(num)
    print(f'Números sorteados: {l}')
        

def numPar(np):
    for v in np:
        if v % 2 == 0:
            lista_par.append(v)
    print(f'Números pares: {lista_par}')

def somaPar(lp):
    soma = sum(lista_par)
    print(f'Soma de todos os números pares: {soma}')


lista_par = []
lista = []

sorteia(lista)
numPar(lista)
somaPar(lista)