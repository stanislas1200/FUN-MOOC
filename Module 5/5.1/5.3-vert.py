def duree(start, end):
    min = 60 - start[1] + end[1]
    h = end[0] - start[0] - 1 if end > start else 24 - start[0] + end[0] - 1
    if min >= 60:
        min -= 60
        h += 1
    return h, min