def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    tot = x20 * 20 + x10 * 10 + x5 * 5 + x2 * 2 + x1 * 1
    if tot < prix:
        r20 = r10 = r5 = r2 = r1 = None
    else:
        reste = tot - prix
        r20 = reste // 20
        reste = reste % 20
        r10 = reste // 10
        reste = reste % 10
        r5 = reste // 5
        reste = reste % 5
        r2 = reste // 2
        reste = reste % 2
        r1 = reste // 1
        reste = reste % 1
    return r20, r10, r5, r2, r1