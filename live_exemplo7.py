# LISTAS

lista = [4, 6, 1, 8, 10]

# Lista vazia
lista = []

#lsita são heterogênea
lista = [4, 6, 2.7, 'teste', 'exemplo']

# alterar
lista = [4, 6, 3, 2, 10]
lista[2] = 300
print(lista)

#consultar um item da lista
print(lista[0])

# append -  insere um item no final da lista
lista = [4, 6, 10, 20]
lista.append(400)
print(lista)
lista.append(500)
print(lista)

# insert - inserir um item em um indice da lista
lista.insert(3, 300)
print(lista)

# pop - remover um item de um indice especifico
lista = [4, 7, 2, 40, 2]
print(lista)
lista.pop(0)
print(lista)

# remove - remove um item pelo valor
lista = [5, 3, 6, 40, 40, 40, 6, 40]
lista.remove(5)
print(lista)

# in - verificar se um item existe em uma lista
lista_nomes = ['paulo', 'ana', 'pedro', 'maria']

nome = input(' Digite um nome para procurar na lista: ')
if nome in lista_nomes:
    print('Nome cadastrado')
else:
    print('Nome não cadastrado')
