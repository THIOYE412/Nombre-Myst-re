""" LE JEU DU NOMBRE MYSTERE """

# SOLUTION
from random import randint

number_to_find = randint(0, 100)
remaining_attemps = 5

print("*** Le jeu du nombre mystère ***")

# Boucle principale
while remaining_attemps > 0:
	print(f"Il te reste {remaining_attemps} essai{'s' if remaining_attemps > 1 else ''}")

	# Saisie de l'utilisateur
	user_choice = input("Devine le nombre : ")
	if not user_choice.isdigit():
		print("Veuillez entrer un nombre valide.")
		continue
	user_choice = int(user_choice)

	if number_to_find > user_choice:	# Plus grand
		print(f"Le nombre mystère est plus grand que {user_choice}")
	elif number_to_find < user_choice:	# Plus petit
		print(f"Le nombre mystère est plus petit que {user_choice}")
	else:	#Egal (succès)
		break

	remaining_attemps -= 1

# Gagné ou perdu
if remaining_attemps == 0:
	print(f"Dommage 😞! Le nombre mystère était {number_to_find}")
else:
	print(f"Bravo 🥳! Le nombre mystère était bien {number_to_find} !")
	print(f"Tu as trouvé le nombre en {6 - remaining_attemps} essai(s)")

print("Fin du jeu 🙂.")
