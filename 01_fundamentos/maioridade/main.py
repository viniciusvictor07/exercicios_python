ano = 2025
maior = 0
menor = 0
for i in range(1, 8):
    nascimento = int(input(f'Digite a data de nascimento da {i}° pessoa: '))
    idade = ano - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} são maiores de idade, {menor} são menores de idade.')