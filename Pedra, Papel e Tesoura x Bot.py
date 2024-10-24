import random


PE = "PE"
PA = "PA"
TE = "TE"


pa = [PE, PA, TE]


regras = {
    PE: TE,  
    TE: PA,  
    PA: PE   
}


rp = str(input("Você quer jogar: (PE)dra, (PA)pel ou (TE)soura? "))
print("Você escolheu: {}".format(rp))


oponente = random.choice(pa)  
print("O Bot escolheu: {}".format(oponente))

if regras[rp] == oponente:
    print(f"{rp} vence {oponente}")
elif regras[oponente] == rp:
    print(f"{oponente} vence {rp}")
else:
    print("Empate!")
