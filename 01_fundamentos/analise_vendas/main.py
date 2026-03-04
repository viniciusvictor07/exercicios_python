fatura_maior = None
fatura_menor = None
dia_maior = None
dia_menor = None
fatura_acima = 0
fatura_abaixo = 0
fatura_total = 0
cliente_total = 0 

dias_venda = int(input('Digite quantos dias de venda foram: '))

for i in range(1, dias_venda+1):
   fatura_dia = float(input(f'Qual valor vendido no {i}° dia? '))
   cliente_atendido = int(input(f'Quantos clientes foram atendidos no {i}° dia? '))    

   # dia com maior/menor faturamento
   if fatura_maior == None:
      fatura_maior = fatura_dia
      fatura_menor = fatura_dia
      dia_maior = i
      dia_menor = i
       
   elif fatura_dia > fatura_maior:
      fatura_maior = fatura_dia
      dia_maior = i
   
   elif fatura_dia < fatura_menor:
      fatura_menor = fatura_dia
      dia_menor = i

   # quantos faturamentos acima de 1000 e abaixo de 500
   if fatura_dia > 1000:
      fatura_acima += 1
   elif fatura_dia < 500:
      fatura_abaixo += 1
   
   # fatura e clientes totais
   fatura_total += fatura_dia
   cliente_total += cliente_atendido

# média de fatura e gasto por cliente

media_fatura = fatura_total / dias_venda
media_gasto = fatura_total / cliente_total

# resultado
print(f'o total faturado entre todos os dias foi: R${fatura_total:.2f}')
print(f'a média de faturamento por dia foi: R${media_fatura:.2f}')
print(f'o dia com o maior faturamento foi: {dia_maior}')
print(f'o dia com o menor faturamento foi: {dia_menor}')
print(f'{fatura_acima} dias tiveram faturamento acima de 1000')
print(f'{fatura_abaixo} dias tiveram faturamento abaixo de 500')
print(f'a média de gasto por cliente foi: R${media_gasto:.2f}')