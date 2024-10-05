# A compra de um veículo pode ser realizada parcelada. Crie um programa que receba o valor de um carro e mostre uma
# tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:

# a) O preço final para compra à vista tem um desconto de 20%:
# b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60:

carro = float(input('Digite o preço do carro: '))
i = 0
desconto = 0.20
acrescimo = 0.03
parcelado = 0
preco_avista = carro - (carro * desconto)

print(f'O preço final á vista com desconto de 20% é: R${preco_avista}')
for i in range(6, 60 + 6, 6):
    preco_parcelado = carro + (carro * acrescimo)
    acrescimo += 0.03
    parcelado = preco_parcelado / i
    print(f'O preço final parcelado em {i} x é de R${preco_parcelado} com parcelas de R${parcelado:.2f}')
