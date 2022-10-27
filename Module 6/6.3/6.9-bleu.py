def compteur_lettres(texte):
    """Counts the number of occurrences of each letter in the text"""
    # Create a dictionary to store the letter counts
    compteur = {}.fromkeys("abcdefghijklmnopqrstuvwxyz", 0)
    # Loop on the text
    for lettre in texte.lower():
        # We add 1 to the letter count if it is in the list
        if lettre in "abcdefghijklmnopqrstuvwxyz":
            compteur[lettre] += 1
    # We return the dictionary
    return compteur