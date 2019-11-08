chiffre = int(input("Entrez un entier strictement positif : "))

liste = []

for i in range(1, chiffre):
    if (i != 1):
        if chiffre % i == 0:
            liste.append(i)

if len(liste) == 0:
    print("Diviseurs propres sans répétition de " + str(chiffre) + " : aucun ! Il est premier")
else:
    print("Divisteurs propres sans répétition de " + str(chiffre) + " " + str(liste))