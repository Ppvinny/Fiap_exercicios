voto1 = input('Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ')
voto2 = input('Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ')
voto3 = input('Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ')
voto4 = input('Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ')
voto5 = input('Informe qual prêmio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO: ')

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Voto inexistente, voto desconsiderado")

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Voto inexistente, voto desconsiderado")

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Voto inexistente, voto desconsiderado")

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Voto inexistente, voto desconsiderado")

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("Voto inexistente, voto desconsiderado")

if playstation > xbox and playstation > nintendo:
        print('O console escolhido foi Playstation')
elif xbox > playstation and xbox > nintendo:
    print('O console escolhido foi xbox')
elif nintendo > xbox and nintendo > playstation:
    print('O console escolhido foi Nintendo')
else:
    print('houve empate, favor entrar em contato com a diretoria')