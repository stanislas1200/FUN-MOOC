def anagrammes(v, w):
    """Renvoie True si v et w sont des anagrammes l'un de l'autre."""
    if len(v) != len(w):
        return False
    for lettre in v:
        if lettre not in w or w.count(lettre) != v.count(lettre):
            return False
    return True

print(anagrammes('bbonjour', 'abonjour'))