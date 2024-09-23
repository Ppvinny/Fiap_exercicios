#faixa de bônus
#> 1000 3gb
#> 500 1,5
#> 200 500mb
#<200 nenhum bonus

pontos = int(input('infome a quantidade de pontos do cliente: '))
if pontos > 1000:
    print('O cliente recebe 3Gb adicionais! ')
else:
    if pontos > 500:
        print('O cliente recebe 1,5Gb adicionais!')
    else:
        if pontos > 200:
            print('O cliente recebe 500Mb adicionais!')
        else:
            print('O cliente não recebe dados adicionais!')