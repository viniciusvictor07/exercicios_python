# EMPRESTIMO

casa =  float(input('Digite o valor da casa: '))
salario =  float(input('Digite o seu salário: '))
anos =  int(input('Digite o quantos anos de pagamento: '))
mes = anos * 12
emp = casa / mes
limite = salario * 0.3  

if emp <=limite:
    situacao = 'igual ou inferior'
    aprovacao = 'concebido'
else:
    situacao = 'superior'
    aprovacao = 'negado'
print(f'Sua casa dividida em {int(mes)} meses fica R${emp:.2f} mensais, sendo {situacao} a 30% do seu salário, logo o empréstimo foi {aprovacao} ')






