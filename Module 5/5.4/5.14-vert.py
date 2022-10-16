def recursive_distance_mots(mot_1, mot_2):
    """Renvoie la distance entre deux mots."""
    if len(mot_1) == 0:
        return len(mot_2)
    if len(mot_2) == 0:
        return len(mot_1)
    if mot_1[-1] == mot_2[-1]:
        return distance_mots(mot_1[:-1], mot_2[:-1])
    return 1 + min(distance_mots(mot_1[:-1], mot_2[:-1]),
                   distance_mots(mot_1[:-1], mot_2),
                   distance_mots(mot_1, mot_2[:-1]))


def distance_mots(mot_1, mot_2):
    """Renvoie la distance entre deux mots."""
    dist = 0
    for i in range(len(mot_1)):
        if i < len(mot_1) and i < len(mot_2) and mot_1[i] != mot_2[i]:
            dist += 1
    return dist
