idade = int(input('Para sua entrada ser permitida, você precisa ser maior idade ou ter autorização. Digite sua idade: '))
autorizacao = input('Você tem autorização? (responda com "sim" ou "nao"): ') 

entrada_idade = idade >= 18
entrada_auto = autorizacao == "sim"

if entrada_auto or entrada_idade: 
    print('Entrada permitida')
else: 
    print('Entrada negada')