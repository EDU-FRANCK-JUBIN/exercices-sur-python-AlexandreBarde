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
    for i in range(2):
        chaine = chaine + random.choice(caracteres_valide)
    return chaine


def proportion(chaine, sequence):
    splitted = chaine.split(sequence)
    nombreOccurence = len(splitted)
    pourcentage = (nombreOccurence / len(chaine)) * 100
    return round(pourcentage, 2)

chaineADN = "attgcaatggtggtacatg"

print("Chaîne : " + str(chaineADN))

char_saisie = saisie()

print("Séquence : " + str(char_saisie))

print("Il y a " + str(proportion(chaineADN, char_saisie)) + "% de \"" + str(char_saisie) + "\" dans votre chaîne.")
