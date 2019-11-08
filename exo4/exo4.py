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


chaineADN = "attgcaatggtggtacatg"

print("Valide ? : " + str(est_valide(chaineADN)))

