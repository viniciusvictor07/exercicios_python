def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(txt.center(tam))
    print('-' * tam)

mensagens = []

while True:
    txt = input('Digite seu texto (ou "sair"): ').upper().strip()
    if txt == "SAIR":
        break
    mensagens.append(txt[:])

for t in mensagens:
    escreva(t)