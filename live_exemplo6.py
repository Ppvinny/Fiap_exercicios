

# range (fim)
# range ( inicio, fim)
# range ( inicio, fim, incremento)

soma = 0
for a in range(10):
    nota = float(input('Digite a nota: '))
    soma += nota

media = soma / 10
print(f'A média é {media}')