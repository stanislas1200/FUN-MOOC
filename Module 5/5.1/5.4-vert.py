import math


def distance_points(points1, points2):
    return math.sqrt((points2[0] - points1[0]) ** 2 + (points2[1] - points1[1]) ** 2)