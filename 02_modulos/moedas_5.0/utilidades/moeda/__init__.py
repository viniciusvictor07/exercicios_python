def metade(p=0, formato=False):
    resp = p / 2
    return resp if not formato else formatar(resp)    

def dobro(p=0, formato=False):
    resp = p * 2
    return resp if not formato else formatar(resp)    
    
def aumentar(p=0, taxa_a=10, formato=False):
    resp = p + (p * taxa_a / 100)
    return resp if not formato else formatar(resp)
def diminuir(p=0, taxa_r=13, formato=False):
    resp = p - (p * taxa_r / 100)
    return resp if not formato else formatar(resp)

def formatar(p=0):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p=0, taxa_a=10, taxa_r=13):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f"Preço analisado: \t{formatar(p)}")
    print(f"Dobro do preço: \t{dobro(p, True)}")
    print(f"Metade do preço: \t{metade(p, True)}")
    print(f"Com {taxa_a}% de aumento: \t{aumentar(p, taxa_a, True)}")
    print(f"Com {taxa_r}% de redução: \t{diminuir(p, taxa_r, True)}")
    print('-' * 30)
