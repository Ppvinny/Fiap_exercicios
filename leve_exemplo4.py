# Solicitar a m idade de 10 pessoas
# calcular a média de idade das pessoas

cont = 0            # contadora
soma = 0            # somadora / acumuladoras

while cont < 10:
    idade = int(input('Digite uma idade: '))
    soma += idade
    cont += 1

media = soma / 10
print(f'A média de idade das pessoas é {media}')
