import math


def distance_points(points1, points2):
    return math.sqrt((points2[0] - points1[0]) ** 2 + (points2[1] - points1[1]) ** 2)


def longueur(*points):
    dist = 0
    for i in range(len(points) - 1):
        dist += distance_points(points[i], points[i + 1])
    return dist