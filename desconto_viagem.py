valor_bruto = float(input('Por favor, informe o valor bruto da viagem: '))
categoria = input('Por favor, informe a categoria: ECONÔMICA, EXECUTIVA ou PRIMEIRA CLASSE')
quantidade_viajantes = int(input('Por favor, informe a quantidade de viajantes'))

valor_desconto = 0
if categoria.upper() == 'ECONÔMICA':
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viajantes >= 4:
        valor_bruto = valor_bruto * 0.05
elif categoria.upper() == 'EXECUTIVA':
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
        valor_bruto = valor_bruto * 0.08
elif categoria.upper() == 'PRIMEIRA CLASSE':
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.1
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
        valor_bruto = valor_bruto * 0.20
else:
    print('Categoria inexistente, não será concedido nenhum desconto')

valor_liquido = valor_bruto - valor_desconto
media_viajante = valor_liquido / quantidade_viajantes

print(f'O valor da viagem é de {valor_bruto}. Após os descontos de R%{valor_desconto}, a viagem custará R${valor_liquido}. Cada passageiro tem um custo médio de R${media_viajante}')