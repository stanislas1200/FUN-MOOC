factorielle = lambda n: n * factorielle(n - 1) if n != 0 else 1


def catalan(n):
    if n <= 1:
        return 1
    ret = (factorielle(2 * n) // (factorielle(n + 1) * factorielle(n)))
    return ret