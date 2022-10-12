def soleil_leve(sunrise, sunset, time_now):
    if sunrise == sunset == 0:
        return True
    elif sunrise <= time_now < sunset:
        return True
    elif sunrise > sunset:
        if time_now < sunset or sunrise <= time_now:
            return True
        else:
            return False
    else:
        return False