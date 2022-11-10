def gagnant(grille):
    """Returns the color of the winner if there is one, or None otherwise."""
    for i in range(6):
        for j in range(7):
            if grille[i][j] != "V":
                if (j <= 3) and (grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3]):
                    return grille[i][j]
                if (i <= 2) and (grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j]):
                    return grille[i][j]
                if (i <= 2) and (j <= 3) and (grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3]):
                    return grille[i][j]
                if (i >= 3) and (j <= 3) and (grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] == grille[i-3][j+3]):
                    return grille[i][j]
    return None