def inventaire(offres, objets):
    """Retourne un dictionnaire contenant les personnes chez qui aller"""
    # Créer un dictionnaire vide
    personnes = set('')
    # Parcourir les offres
    for objet, personne in offres.items():
        # Si l'objet est dans la liste des objets
        if objet in objets:
            # Ajouter la personne à la liste
            personnes.add(personne)
    # Retourner le dictionnaire
    return personnes