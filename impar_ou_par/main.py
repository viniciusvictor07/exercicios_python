from random import randint 
vitorias = 0

while True:
    num_maquina = randint(1,5)
    num_usuario = int(input('Digite um valor: '))
    escolha_usuario = (input('Escolha par ou ímpar [P/I]: ')).upper().strip()[0]
    soma = num_maquina + num_usuario
    
    # par ou impar
    if soma % 2 == 0:
        resultado = 'P'
    if soma % 2 != 0:
        resultado = 'I'
    # verificar input do jogador
    if escolha_usuario == resultado:
        print(f'VENCEU! A soma do número do computador ({num_maquina}) e o do usuário ({num_usuario}) é {soma}, sendo um número par.')
        vitorias += 1
    
    if escolha_usuario != resultado:
        print(f'Perdeu! A soma do número do computador ({num_maquina}) e o do usuário ({num_usuario}) é {soma}, sendo um número ímpar.')
        break     
print(f'O usuário venceu {vitorias} vezes.')