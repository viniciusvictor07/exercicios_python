soma_idade = 0
f_menor = 0
idade_velho = None
nome_velho = None

quantia = int(input('Digite quantas pessoas: '))

for i in range(1, quantia+1):
   nome = (input(f'Digite o nome da {i}° pessoa: '))   
   idade = int(input(f'Digite a idade de {nome}: '))
   sexo = input(f'Digite o sexo de {nome} (M/F): ').strip().upper()
   soma_idade += idade
   if sexo == 'M': # descobrir qual é o homem mais velho
      if nome_velho is None:
         nome_velho = nome
         idade_velho = idade
      elif idade > idade_velho:
         nome_velho = nome
         idade_velho = idade
   if sexo == 'F' and idade < 20: # quantas F são menores de 20 anos
      f_menor += 1

media = soma_idade / quantia

print(f'A média de todas as idades é {media:.1f} anos') 
if idade_velho is not None:
   print(f'o homem mais velho é {nome_velho}')
else:
   print('Nenhum homem foi encontrado')
if f_menor == 0:
   print('Nenhuma mulher com menos de 20 anos foi encontrada')
else:
   print(f'{f_menor} mulheres são menores de 20 anos')