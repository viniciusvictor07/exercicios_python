def leiaInt(msg):
    while True:
        try:
            num_int = int(input(msg))
            return num_int
        
        except ValueError:
            print('Isso não é um número inteiro. Tente novamente.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
            return 0

def leiaFloat(msg):
    while True:
        try:
            num_float = float(input(msg))
            return num_float
        
        except ValueError:
            print('Isso não é um número real. Tente novamente.')
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados!')
            return 0.0