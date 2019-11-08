import random

def est_valide(chaine):
    splitted = list(chaine)

    valeur = True

    for i in range(len(splitted)):
        if splitted[i] == 'a' or splitted[i] == 't' or splitted[i] == 'g' or splitted[i] == 'c':
            valeur = True
        else:
            valeur = False
            break
    return valeur

def saisie():
    caracteres_valide = ['a', 't', 'g', 'c']
    chaine = ""
    for i in range(4):
            chaine = chaine + random.choice(caracteres_valide)
    return chaine

print(saisie())

chaineADN = "attgcaatggtggtacatg"

print("Valide ? : " + str(est_valide(chaineADN)))

