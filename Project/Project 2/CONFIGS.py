ZONE_PLAN_MINI = (-240, -240)  # Coin inférieur gauche de la zone d'affichage du plan
ZONE_PLAN_MAXI = (50, 200)  # Coin supérieur droit de la zone d'affichage du plan
POINT_AFFICHAGE_ANNONCES = (-240, 240)  # Point d'origine de l'affichage des annonces
POINT_AFFICHAGE_INVENTAIRE = (70, 210)  # Point d'origine de l'affichage de l'inventaire



# Couleur et dimension du personnage
RATIO_PERSONNAGE = 0.9  # Rapport entre diamètre du personnage et dimension des cases
POSITION_DEPART = (0, 1)  # Porte d'entrée du château

# Désignation des fichiers de données à utiliser
fichier_plan = 'plan_chateau.txt'
fichier_questions = 'dico_portes.txt'
fichier_objets = 'dico_objets.txt'

# Size of the window
WINDWOS_SIZE = (480, 555)
BORDER_SIZE = 15

# Size of the Announcements
ANNOUNCEMENT_SIZE = (WINDWOS_SIZE[0] - BORDER_SIZE * 2, WINDWOS_SIZE[1] / 100 * 15)
ANNOUNCEMENT_COORD = (-WINDWOS_SIZE[0] / 2 + BORDER_SIZE, WINDWOS_SIZE[1] / 2 - BORDER_SIZE - ANNOUNCEMENT_SIZE[1])

# Size of the inventory
INVENTORY_SIZE = ((WINDWOS_SIZE[0] - BORDER_SIZE * 3) / 100 * 30, WINDWOS_SIZE[1] - BORDER_SIZE * 3 - ANNOUNCEMENT_SIZE[1])
INVENTORY_COORD = (WINDWOS_SIZE[0] / 2 - BORDER_SIZE - INVENTORY_SIZE[0], -WINDWOS_SIZE[1] / 2 + BORDER_SIZE)

# Size of the board
BOARD_SIZE = (WINDWOS_SIZE[0] - BORDER_SIZE * 3 - INVENTORY_SIZE[0], WINDWOS_SIZE[1] - BORDER_SIZE * 3 - ANNOUNCEMENT_SIZE[1])
BOARD_COORD = (-WINDWOS_SIZE[0] / 2 + BORDER_SIZE, -WINDWOS_SIZE[1] / 2 + BORDER_SIZE)

theme = "discord"
# Color palette
if theme == "discord":
    COULEUR_CASES = '#ffffff'
    COULEUR_MUR = '#23272a'
    COULEUR_OBJECTIF = '#fee75c'
    COULEUR_PORTE = '#3c3c3c'
    COULEUR_OBJET = '#7289da'
    COULEUR_VUE = '#99aab5'
    COULEUR_EXTERIEUR = '#ffffff'
    COULEUR_BOX = '#2c2f33'
    COULEUR_PERSONNAGE = '#5865f2'
    COULEUR_TEXTE = '#ffffff'
else:
    # Les valeurs ci-dessous définissent les couleurs des cases du plan
    COULEUR_CASES = 'white'
    COULEUR_MUR = 'grey'
    COULEUR_OBJECTIF = 'yellow'
    COULEUR_PORTE = 'orange'
    COULEUR_OBJET = 'green'
    COULEUR_VUE = 'wheat'
    COULEUR_EXTERIEUR = 'white'
    COULEUR_BOX = '#2c2f33'
    COULEUR_PERSONNAGE = 'red'
    COULEUR_TEXTE = 'black'