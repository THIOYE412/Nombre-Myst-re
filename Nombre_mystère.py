""" LE JEU DU NOMBRE MYSTERE """

import random

print("*** LE JEU DU NOMBRE MYSTERE ***\n")
Nbre_essais = 5
N_e = 0
Nbre_mystere = random.randrange(0, 101)

# BOUCLE PRINCIPALE

while True:
	essai = print(f"Il te reste {Nbre_essais} essai(s)") 

	if Nbre_essais == 0:
		print(f"Dommage 😞! Le nombre mystère était {Nbre_mystere}")
		break
	MYSTERE = input("Devine le nombre : ")
	if not MYSTERE.isdigit():
		print("Veuillez entrez un nombre valide")
		continue
	elif MYSTERE.isdigit():
		N_e += 1 
		if int(MYSTERE) == Nbre_mystere:
			print(f"Bravo 👏🥳! Le nombre mystère était bien {MYSTERE}.")
			print("Tu as trouvé le nombre en {N_e} essai(s).")
			break
		elif int(MYSTERE) > Nbre_mystere:
			print(f"Le nombre mystère est plus petit que {MYSTERE}")
		elif int(MYSTERE) < Nbre_mystere:
			print(f"Le nombre mystère est plus grand que {MYSTERE}")
	Nbre_essais -= 1

print("Fin du jeu 🙂 !")