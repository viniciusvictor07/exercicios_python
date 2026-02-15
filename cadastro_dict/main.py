lista_pessoas = []
lista_media = []
lista_mulher = []
soma_idade = 0

while True:
    dict_pessoas = {}
    dict_pessoas['nome'] = input('Digite o nome: ')
    dict_pessoas['sexo'] = input('Digite o sexo [M/F]: ').upper().strip()
    dict_pessoas['idade'] = int(input('Digite a idade: '))
    lista_pessoas.append(dict_pessoas)
    soma_idade += dict_pessoas['idade']
    if dict_pessoas['sexo'] == 'F':
        lista_mulher.append(dict_pessoas)

    resp = input('Deseja continuar? [S/N]: ').upper().strip()
    if resp == 'N':
        break

media = soma_idade / len(lista_pessoas)

print(f'{len(lista_pessoas)} pessoas foram cadastradas. ')
print(f'Mulheres cadastradas: {lista_mulher}')

for p in lista_pessoas:
    if p['idade'] > media:
        lista_media.append(p.copy())
print(f'As pessoas com idade acima da média são: {lista_media}')
