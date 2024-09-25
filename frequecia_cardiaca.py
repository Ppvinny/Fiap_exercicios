# idade BPM
# Até 2 anos 120 a 140
# De 8 anos até 17 anos 80 a 100
# Adulto sedentario 70 a 80
# idoso 50 a 60

print('VERIFICADOR DE FREQUÊNCIA CARDÍACAS')
idade = int(input('Por favor, informe a sua idade: '))
bpm = int(input('Por favor, informe seu batimentos cardiacos:  '))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print('Frequencia cardiaca adequada')
    else:
        print('Frequencia cardiaca inadequada')
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print('Frequencia cardiaca adequada')
    else:
        print('Frequencia cardiaca inadequada')
elif idade >= 18 and idade <= 60:
    if bpm >= 70 and bpm <= 100:
        print('Frequencia cardiaca adequada')
    else:
        print('Frequencia cardiaca inadequada')
elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print('Frequencia cardiaca adequada')
    else:
        print('Frequencia cardiaca inadequada')
else:
    print('Não existe dados para a idade indicada')