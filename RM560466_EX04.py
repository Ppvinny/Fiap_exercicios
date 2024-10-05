menu = 0
ir = 0
dias_investidos = 0
resgate = 0

while menu != 4:
    menu = int(
        input('Escolha o tipo de investimento: \n1. CDB \n2. LCI \n3. LCA \n4. Sair \nDigite o tipo de investimento: '))

    if menu == 1 or menu == 2 or menu == 3:
        resgate = float(input('Digite o valor a ser resgatado: '))
        dias_investido = int(input('Digite o número de dias que o valor permaneceu investido: '))


        if menu == 1 and dias_investido <= 180:
            ir = resgate * 0.225
        elif menu == 1 and dias_investido <= 360:
            ir = resgate * 0.20
        elif menu == 1 and dias_investido <= 720:
            ir = resgate * 0.175
        elif menu == 1 and dias_investido > 720:
            ir = resgate * 0.15

        print(f'O valor de imposto de renda a ser pago é: R$ {ir:.2f}')
        break

    elif menu == 4:
        print("Saindo do programa.")
        break
    else:
        print('Entrada inválida, por favor digite um número entre 1 e 4.')
