PE = "PE"
PA = "PA"
TE = "TE"

PE > TE
TE > PA
PA > PE
while True:
    n1 = str(input("Digite sua escolha: (Pe)dra, (PA)pel ou (Te)soura? "))

    n2 = str(input("Digite sua escolha: (Pe)dra, (PA)pel ou (Te)soura? "))


    if  n1 > n2:
        print("Player 1 ganhou!!")
    elif n2 > n1:
        print("Player 2 ganhou!!")
    else:
        print("Empate")
