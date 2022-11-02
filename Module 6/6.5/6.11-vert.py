import math


def bonne_planete(diametre):
    """Returne True if the planet is big enought for 50m^^2 of surface"""
    return diametre ** 2 * math.pi >= 50 * 1000
