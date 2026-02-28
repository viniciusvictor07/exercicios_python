def leiaNum(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print('Valor inválido! Digite um número inteiro.')

n1 = leiaNum('Digite um número: ')
print(f'Você digitou o número {n1}.')