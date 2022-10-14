def next_prime(nb):
    while True:
        nb += 1
        for i in range(2, nb):
            if nb % i == 0:
                break
        else:
            return nb


def prime_numbers(nb):
    prime = [2]
    if type(nb) != int or int(nb) < 0:
        return None
    if int(nb) == 0:
        return []
    while int(len(prime)) < int(nb):
        prime.append(next_prime(prime[-1]))
    return prime
