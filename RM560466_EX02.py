# variaveis
carro = float(input('Digite o preço do carro: '))
i = 0
desconto = 0.20
acrescimo = 0.03
parcelado = 0
preco_avista = carro - (carro * 20 / 100)

lista = [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60]

for i in lista:
   if i == 0:
       print(f'O preço final á vista com desconto de 20% é: R${preco_avista}')
   else:
       preco_parcelado = carro + (carro * acrescimo)
       acrescimo += 0.03
       parcelado = preco_parcelado / i
       print(f'O preço final parcelado em {i} x é de R${preco_parcelado} com parcelas de R${parcelado:.2f}')