num = int(input('Digite um número inteiro: '))
if num < 2:
    primo = False
else:
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break

if primo:
    print('É um número primo')
else:
    print('Não é um número primo')