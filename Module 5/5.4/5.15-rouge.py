def distance_mots(mot_1, mot_2):
    """Renvoie la distance entre deux mots."""
    dist = 0
    for i in range(len(mot_1)):
        if i < len(mot_1) and i < len(mot_2) and mot_1[i] != mot_2[i]:
            dist += 1
    return dist


def correcteur(mot, liste_mots):
    """Renvoie le mot de la liste qui est le plus proche du mot."""

    return min(liste_mots, key=lambda mot_liste: distance_mots(mot, mot_liste))