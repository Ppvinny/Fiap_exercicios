#solicitando os dados do cliente
valor_compra = float(input('informe o valor da compra: '))
cupom = input('Digite o cupom de desconto: ')
#realizando o teste lógico com o cupom em maiúsculas
if cupom.upper() == 'NIVER10':
    #cálculo de 10% de desconto
    valor_final = valor_compra * 0.9
else:
    valor_final = valor_compra
    print('Cupom inválido')
#exibindo o valor final da compra
print(f'O valor final é {valor_final}')