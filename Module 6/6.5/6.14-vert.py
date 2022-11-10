def placer_pion(couleur, colonne, grille):
    """Places a pawn of the given color in the given column.
    The grid is modified accordingly.
    """
    if (colonne < 0) or (colonne > 6 or couleur not in ["R", "J"]):
        return False, grille
    for i in range(6):
        if grille[i][colonne] == "V":
            grille[i][colonne] = couleur
            return True, grille
    return False, grille