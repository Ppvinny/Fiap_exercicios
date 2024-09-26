#variaveis
colaboradores = int(input('Informe o numero de colaboradores: '))
segunda_f = 0
terca_f = 0
quarta_f = 0
quinta_f = 0
sexta_f = 0

i = 1

while i <= colaboradores:
    voto = input('Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ')
    if voto.lower() == 'segunda-feira':
        segunda_f += 1
        i += 1
    elif voto.lower() == 'terça-feira':
        terca_f += 1
        i += 1
    elif voto.lower() == 'quarta-feira':
        quarta_f += 1
        i += 1
    elif voto.lower() == 'quinta-feira':
        quinta_f += 1
        i += 1
    elif voto.lower() == 'sexta-feira':
        sexta_f +=1
        i += 1
    elif voto.lower() != 'segunda-feira' or 'terça-feira' or 'quarta-feira' or 'quinta-feira' or 'sexta-feira':
        print('Voto inválido, digite novamente')

if (segunda_f > terca_f and segunda_f > quarta_f and
        segunda_f > quinta_f and segunda_f > sexta_f):
    print('O dia escolhido pelos colaboradores é: Segunda-feira')
elif (terca_f > segunda_f and terca_f > quarta_f and
      terca_f > quinta_f and terca_f > sexta_f):
    print('O dia escolhido pelos colaboradores é: Terça-feira')
elif (quarta_f > segunda_f and quarta_f > terca_f and
      quarta_f > quinta_f and quarta_f > sexta_f):
    print('O dia escolhido pelos colaboradores é: Quarta-feira')
elif (quinta_f > segunda_f and quinta_f > terca_f and
      quinta_f > quarta_f and quinta_f > sexta_f):
    print('O dia escolhido pelos colaboradores é: Quinta-feira')
elif (sexta_f > segunda_f and sexta_f > terca_f and
      sexta_f > quarta_f and sexta_f > quinta_f):
    print('O dia escolhido pelos colaboradores é: Sexta-feira')
else:
    print('Houve um empate entre os dias mais votados, reiniciar o programa!')