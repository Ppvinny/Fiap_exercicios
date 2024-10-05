
while True:     # loop infinito
    idade = int(input('digite a idade: '))
    if idade >= 0:
        break
    else:
        print('Erro. A idade deve ser maior ou igual a zero')

print(f'A sua idade é de {idade} anos')
