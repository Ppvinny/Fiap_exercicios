# preencher lista com nome de várias pessoas
# inserir os nomes em uma lista

lista_nomes = []

while True:
    nome = input('Digite o nome:')
    if nome == '':
        break
    if nome not in lista_nomes:     # verifica na lista
        lista_nomes.append(nome)    # inserindo o nome na lista
    else:
        print('nome já cadastrado')

# len - verifica o tamanho da uma lista
quantidade = len(lista_nomes)
print(f'Quantidade de pessoas cadastradas: {quantidade}')

# percorrer os itens da lista:
for indice in range(quantidade): # indice = 0,1,2,3,4,5,6,7,8,9
    print(lista_nomes[indice])