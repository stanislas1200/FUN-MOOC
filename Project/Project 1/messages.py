############################
ENDC = '\033[0m'
FAIL = '\033[91m'
OKGREEN = '\033[92m'
PURPLE = '\033[95m'
WARNING = '\033[93m'

message_1 = """Bonjour ! Bienvenue au jeu du Sac de Billes. 
Je suis une IA mais j'aimerais voir si tu peux gagner contre moi !"""
entree_1 = "Entrez la graine: "
message_2 = WARNING + """Voici un rappel des règles :
Tout d'abord, tu vas choisir combien de billes sont dans le sac.
Chacun son tour (je te laisse commencer), on en retire 1, 2, 3 ou 4.
Celui qui retire la dernière bille a perdu.""" + ENDC
entree_2 = """A présent, merci de m'indiquer combien de billes tu choisis 
au total dans le sac avant de lancer la partie. 
Minimum 6 - Maximum 40 : """
message_3 = "Que la partie commence !"
message_4 = "C'est à toi de jouer. Il reste {0} billes."
entree_3 = "Combien de billes retires-tu ? 1, 2, 3 ou 4 ? "
message_5 = "Il reste à présent {0} billes."
message_6 = "C'est à moi de jouer."
message_7 = "J'ai choisi de retirer {0} bille(s)."
message_8 = """Il ne reste qu'une seule bille dans le sac... 
et c'est à moi de jouer... 
%sC'est bon, tu as gagné ! Bravo !%s""" % (OKGREEN, ENDC)
entree_4 = OKGREEN + "Veux-tu jouer une nouvelle partie ? oui/non : " + ENDC
message_9 = """Il ne reste qu'une seule bille dans le sac... 
et c'est à toi de jouer... 
%sJ'ai donc gagné !%s""" % (FAIL, ENDC)
message_10 = PURPLE + "Je prends cela pour un oui. ^-^" + ENDC
message_11 = PURPLE + "Dommage, je m'amuse bien avec toi ! Au revoir ^-^)" + ENDC
error_1 = FAIL + "Erreur : graine invalide. Default 0." + ENDC
error_2 = FAIL + "Erreur : nombre de billes invalide." + ENDC
error_3 = FAIL + "Erreur : veuillez entrer un entier!" + ENDC
error_4 = FAIL + "Erreur : Tu n'as pas respecté les règles." + ENDC
####################################
