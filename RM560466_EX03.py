# – Na oferta de um produto de crédito aos clientes, três informações são muito importantes apresentar ao cliente:
# valor da dívida, a taxa de juros e o número de parcelas para pagamento do empréstimo contraído junto à Fintech.
# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:

# Valor da dívida, valor do juros, quantidade de parcelas e valor da parcela.

valor_inicial = float(input('Digite o valor da dívida: '))
juros = 0
parcelas = 0
valor_parcela = 0

for parcelas in [1, 3, 6, 9, 12]:
    if parcelas == 1:
        juros = 0
    elif parcelas == 3:
        juros = 0.10 * valor_inicial
    elif parcelas == 6:
        juros = 0.15 * valor_inicial
    elif parcelas == 9:
        juros = 0.20 * valor_inicial
    elif parcelas == 12:
        juros = 0.25 * valor_inicial

    divida = valor_inicial + juros
    valor_parcela = divida / parcelas

    print(f'Total:R$ {divida} Juros:R$ {juros} Número de parcelas: {parcelas} Valor da Parcela:R${valor_parcela:.2f}')