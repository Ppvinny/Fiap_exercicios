# solicitar a idade de 10 pessoas
# Contar quantas pessoas menores de idade
# Contar quantas pessoas maiores de idade


cont = 0  #contadora
conta_menores = 0  #contadora
conta_maiores = 0  #contadora
while cont < 10:
    idade = int(input('Digite a idade: '))
    if idade < 18:
        conta_menores += 1
    else:
        conta_maiores += 1
    cont += 1

print(f'Quantidade de pessoas menores de idade: {conta_menores}')
print(f'Quantidade de pessoas maiores de idade: {conta_maiores}')
