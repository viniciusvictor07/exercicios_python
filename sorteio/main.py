from random import randint
from operator import itemgetter
from time import sleep

lista = {}
for i in range(1,5):
    lista[f'jogador{i}'] = randint(1,6)
    
for j, n in lista.items():
    print(f'o {j} tirou o número {n}')
    sleep(1)
print('--RANKING--')
sleep(2)

ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)

for i, j in enumerate(ranking):
    print(f'{i+1}º lugar pro {j[0]} com o número {j[1]}')
    sleep(1)
print('FIM!'.center(35))