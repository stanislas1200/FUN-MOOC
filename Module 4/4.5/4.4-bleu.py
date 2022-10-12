import random


def alea_dice(s):
    random.seed(s)
    return True if random.randint(1, 6) * 100 + random.randint(1, 6) * 10 + random.randint(1, 6) in [421, 142, 214, 241,
                                                                                                     412,
                                                                                                     124] else False
