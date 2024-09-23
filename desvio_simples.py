#Pedir que o usuário digite o nome do funcionário
nome = input('Infome o nome do funcionário: ')
#Pedir que o usuário digite o salário do funcionário
salario = float(input('Informe o salário do funcionário: '))
#Caso o salário seja negativo, alertar o usuário
if salario < 0:
    #salario = salario * -1
    #Função Python 'abs' transforma a entrada e saida em positivo
    salario = abs(salario)
    print('Atenção, foi informado um salário negativo!')
#Exibir o salario armazenado
print(f'O funcionário {nome} tem um salário de R${salario}')