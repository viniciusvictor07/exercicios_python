def metade(p, formato=False):
    resp = p / 2
    return resp if not formato else formatar(resp)    

def dobro(p, formato=False):
    resp = p * 2
    return resp if not formato else formatar(resp)    
    
def aumentar(p, formato=False):
    resp = p + (p * 10 / 100)
    return resp if not formato else formatar(resp)
def diminuir(p, formato=False):
    resp = p - (p * 13 / 100)
    return resp if not formato else formatar(resp)

def formatar(p):
    return f'R${p:.2f}'.replace('.', ',')