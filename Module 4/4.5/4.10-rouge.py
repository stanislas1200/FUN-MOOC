import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2


def bat(a, b):
    if a == b:
        return -1
    elif a == PIERRE:
        return False if b == FEUILLE else True
    elif a == FEUILLE:
        return False if b == CISEAUX else True
    elif a == CISEAUX:
        return False if b == PIERRE else True


s = int(input())
random.seed(s)
lst = [0,0,0,0,0]
points = 0
for i in range(5):
    lst[i] = int(input())
for i in range(5):
    coup_o = random.randint(0, 2)
    if bat(lst[i], coup_o) == -1:
        pass
    elif bat(coup_o, lst[i]):
        points -= 1
    elif bat(lst[i], coup_o):
        points += 1
    print(f"{'Pierre' if coup_o == PIERRE else 'Feuille' if coup_o == FEUILLE else 'Ciseaux'} {'annule' if bat(coup_o, lst[i]) == -1 else 'est battu par' if not bat(coup_o, lst[i]) else 'bat'} {'Pierre' if lst[i] == PIERRE else 'Feuille' if lst[i] == FEUILLE else 'Ciseaux'} : {points}")
if points > 0:
    print("Gagné")
elif points < 0:
    print("Perdu")
else:
    print("Nul")