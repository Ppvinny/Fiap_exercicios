minutos = int(input('informe o numero dos minutos do horario atual '))
fatorial = minutos
for numero in range(1, minutos):
    fatorial = fatorial * numero
print(f'A senha pe liberdade{fatorial}')