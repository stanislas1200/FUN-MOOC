def placer_pion(couleur, colonne, grille):
    """Place un pion de la couleur donnée dans la colonne donnée.
    La grille est modifiée en conséquence.
    """
    if (colonne < 0) or (colonne > 6 or couleur not in ["R", "J"]):
        return False, grille
    for i in range(6):
        if grille[i][colonne] == "V":
            grille[i][colonne] = couleur
            return True, grille
    return False, grille