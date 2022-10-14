
def plus_grand_bord(w):
    """Retourne le plus grand bord commun de w."""
    born = ''
    x = 0
    for i in range(len(w)):
        if w[0] == w[i]:
            x += 1
    if x == len(w):
        return w[:-1]
    rn = len(w)//2 if len(w) % 2 == 0 else len(w)//2 + 1
    for i in range(rn):
        if w[:i+1] == w[-i-1:]:
            born = w[:i+1]
    return born