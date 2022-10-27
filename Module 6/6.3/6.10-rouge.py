def valeurs(dico):
    """Return a liste of the value of a dictionary sorted by the key"""
    return [dico[key] for key in sorted(dico.keys())]

print(valeurs({'three': 'trois', 'two': 'deux', 'one': 'un'}))