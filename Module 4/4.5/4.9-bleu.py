def bat(a, b):
    if a == 0:
        return False if b == 1 or b == 0 else True
    elif a == 1:
        return False if b == 2 or b == 1 else True
    elif a == 2:
        return False if b == 0 or b == 2 else True