import math

rayon = float(input("Rayon ?"))
hauteur = float(input("Hauteur ?"))

volume = (math.pi * (rayon ** 2) * hauteur) / 3

print("Volume : " + str(volume))