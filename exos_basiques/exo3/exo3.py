chiffre = int(input(""))

liste = 0
valeur = []

for i in range(chiffre):
    tmp = 1
    for j in range(1, i):
        tmp = tmp * j
    oui = 1 / tmp
    liste = liste + oui
    print(liste - 1)

valeur.append(liste - 1)
valeur.append(2.71828182845904523536 - valeur[0])
print(valeur)
