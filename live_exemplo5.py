# Solicitar a m idade de várias pessoas
# calcular a média de idade das pessoas

cont = 0            # contadora
soma = 0            # somadora / acumuladora

while True:  #loop infinito
    idade = int(input('Digite uma idade: '))
    if idade < 0:
        break # interrompendo a execução
    soma += idade
    cont += 1

media = soma / cont
print(f'A média de idade das pessoas é {media}')
