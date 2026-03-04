def atualizar_placar(time, gols=0, var="Não acionado"):
    return f"PLACAR: {time} fez {gols} gol(s). | VAR: {var}"


while True:
    time = input('Digite o nome do time: ')
    gols = input('Digite o número de gols (deixe vazio para 0): ')
    var = input('Digite o status do VAR (deixe vazio para "Não acionado"): ')
    
    if gols.isnumeric():
        gols = int(gols)
        if var.strip() == '':
            print(atualizar_placar(time, gols))
        else:
            print(atualizar_placar(time, gols, var))
    
    else:
        if var.strip() == '':
            print(atualizar_placar(time))
        else:
            print(atualizar_placar(time, var=var))

    resp = input('Deseja continuar? [S/N] ').upper().strip()
    if resp == 'N':
        break