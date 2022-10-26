def top_3_candidats(moyennes):
    """Retourne les 3 meilleurs candidats à partir d'un dictionnaire de candidats et de moyennes"""
    # Indexer la liste
    lst_value = list(moyennes.values())
    lst_key = list(moyennes.keys())
    # Créer une liste des moyennes
    liste = lst_value.copy()
    # Trier la liste
    liste.sort(reverse=True)
    # Retourner les 3 meilleurs candidats
    return lst_key[(lst_value.index(liste[0]))], lst_key[(lst_value.index(liste[1]))], lst_key[(lst_value.index(liste[2]))]