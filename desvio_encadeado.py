#faixa de bônus
#> 1000 3gb
#> 500 1,5
#> 200 500mb
#<200 nenhum bonus

pontos = int(input('informe a quantidade de pontos do cliente: '))
if pontos >= 1000:
    print('O cliente recebe 3Gb adicionais! ')
elif pontos > 500:
    print('O cliente recebe 1,5Gb adicionais!')
elif pontos > 200:
    print('O cliente recebe 500m adicionais!')
else:
    print('O cliente não recebe dados adicionais!')