quantidade_alimento = int(input('Quanto alimentos você consumiu hoje? '))
total_calorias = 0
for alimento in range(1, quantidade_alimento + 1, 1):
    caloria = int(input(f'informe a quantidade de calorias do alimento {alimento}: '))
    total_calorias = total_calorias + caloria
print(f'Foram consumidas {total_calorias} calorias ao longo do dia!')