# Quantos funcionários 
num_fun = int(input("Quantos funcionários? "))

# Dados
for i in range(num_fun):
    nome = input("Qual o nome? ")
    horas = int(input("Quantas horas? "))
    valor = int(input("Qual valor? "))
    vendas = int(input("Quantas vendas? "))
    salario = horas * valor

# Conta do salário
    if salario >= 3000 and vendas >= 50: 
        bonus = ("Bônus máximo")
    elif salario >= 2000 and vendas >=30:
        bonus = ("Bônus médio")
    else:  
        bonus = ("Sem Bônus")

# Resultado do salário     
    print(f"\nNome: {nome}\nSalário: R$ {salario:.2f}\nBônus: {bonus}\n")
