def metade(p):
    return p / 2


def dobro(p):
    return p * 2
    
    
def aumentar(p):
    return p + (p * 10 / 100)


def diminuir(p):
    return p - (p * 13 / 100)


def formatar(p):
    return f'R${p:.2f}'.replace('.', ',')