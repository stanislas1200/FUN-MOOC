def intersection(v, w):
    """Renvoie l'intersection de v et w."""
    biggest = ''
    for i in range(len(v)):
        for j in range(len(w)):
            a = 0
            new = ''
            while i+a < len(v) and j+a < len(w) and v[i+a] == w[j+a]:
                new += v[i+a]
                a += 1
            if len(new) > len(biggest):
                biggest = new
    return biggest