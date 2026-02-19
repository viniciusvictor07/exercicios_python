def area(l, c):
    total_area = l * c
    print(f'A área de um terreno {l}x{c} é de {total_area}m²')

l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))

area(l,c)