idade = int(input('digite a idade: '))


while idade < 0:
    print('Erro. A idade deve ser maior ou igual a zero')
    idade = int(input('digite a idade: '))

print(f'A sua idade é de {idade} anos')