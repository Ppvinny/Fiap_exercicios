
def soma(a, b):
    c = a + b
    return c

while True:
    x = int(input('informe um numero: '))
    if x == 0:
        break
    y = int(input('infome outro numero: '))
    z = soma(x, y) # variavel z recebe o retorno da def
    print(f'soma: {z}')

