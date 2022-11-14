
# Dimension du personnage
RATIO_PERSONNAGE = 0.8  # Rapport entre diamètre du personnage et dimension des cases
POSITION_DEPART = (0, 1)  # Porte d'entrée du château

# Désignation des fichiers de données à utiliser
fichier_plan = 'plan_chateau.txt'
fichier_questions = 'dico_portes.txt'
fichier_objets = 'dico_objets.txt'

# Size of the window
WINDOW_SIZE = (480, 555)
BORDER_SIZE = 15

# Size of the Announcements
ANNOUNCEMENT_SIZE = (WINDOW_SIZE[0] - BORDER_SIZE * 2, WINDOW_SIZE[1] / 100 * 15)
ANNOUNCEMENT_COORD = (-WINDOW_SIZE[0] / 2 + BORDER_SIZE, WINDOW_SIZE[1] / 2 - BORDER_SIZE - ANNOUNCEMENT_SIZE[1])

# Size of the inventory
INVENTORY_SIZE = ((WINDOW_SIZE[0] - BORDER_SIZE * 3) / 100 * 30, WINDOW_SIZE[1] - BORDER_SIZE * 3 - ANNOUNCEMENT_SIZE[1])
INVENTORY_COORD = (WINDOW_SIZE[0] / 2 - BORDER_SIZE - INVENTORY_SIZE[0], -WINDOW_SIZE[1] / 2 + BORDER_SIZE)

# Size of the board
BOARD_SIZE = (WINDOW_SIZE[0] - BORDER_SIZE * 3 - INVENTORY_SIZE[0], WINDOW_SIZE[1] - BORDER_SIZE * 3 - ANNOUNCEMENT_SIZE[1])
BOARD_COORD = (-WINDOW_SIZE[0] / 2 + BORDER_SIZE, -WINDOW_SIZE[1] / 2 + BORDER_SIZE)

ANNOUNCEMENT_TEXT_SIZE = ANNOUNCEMENT_SIZE[0]/30
INVENTORY_TEXT_SIZE = INVENTORY_SIZE[0]/12

LEVEL_NUMBER = 0

theme = "discord"
# Color palette
COULEUR_MISSING = "#660066"
if theme == "discord":
    COULEUR_CASES = '#424549'
    COULEUR_MUR = '#1e2124'
    COULEUR_OBJECTIF = '#bea925'
    COULEUR_PORTE = '#c27a2c'
    COULEUR_OBJET = '#7289da'
    COULEUR_VUE = '#99aab5'
    COULEUR_EXTERIEUR = '#ffffff'
    COULEUR_BOX = '#36393e'
    COULEUR_PERSONNAGE = '#5865f2'
    COULEUR_TEXTE = '#ffffff'
elif theme == "colorswall":
    COULEUR_CASES = '#b4c8c8'
    COULEUR_MUR = '#042e27'
    COULEUR_OBJECTIF = '#f4d47c'
    COULEUR_PORTE = '#245454'
    COULEUR_OBJET = '#90f545'
    COULEUR_VUE = '#6d949c'
    COULEUR_EXTERIEUR = '#ffffff'
    COULEUR_BOX = '#245454'
    COULEUR_PERSONNAGE = '#fa4454'
    COULEUR_TEXTE = '#ffffff'
elif theme == "purple":
    COULEUR_CASES = '#ba68c8'
    COULEUR_MUR = '#4a148c'
    COULEUR_OBJECTIF = '#f9e46a'
    COULEUR_PORTE = '#6a1b9a'
    COULEUR_OBJET = '#d500f9'
    COULEUR_VUE = '#e1bee7'
    COULEUR_EXTERIEUR = '#ffffff'
    COULEUR_BOX = '#3e394c'
    COULEUR_PERSONNAGE = '#ab3cfc'
    COULEUR_TEXTE = '#ffffff'
else:
    COULEUR_CASES = 'white'
    COULEUR_MUR = 'grey'
    COULEUR_OBJECTIF = 'yellow'
    COULEUR_PORTE = 'orange'
    COULEUR_OBJET = 'green'
    COULEUR_VUE = 'wheat'
    COULEUR_EXTERIEUR = 'white'
    COULEUR_BOX = '#ffffff'
    COULEUR_PERSONNAGE = 'red'
    COULEUR_TEXTE = 'black'