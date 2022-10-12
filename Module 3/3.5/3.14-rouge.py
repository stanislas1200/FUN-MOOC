import random
answer = random.randint(0, 100)

for i in range(6):
    guess = int(input())
    if guess == answer:
        print("Gagné en ", i+1, " essai(s) !")
        exit()
    elif i == 5:
        print("Perdu ! Le secret était", answer)
        exit()
    elif guess < answer:
        print("Trop petit")
    else:
        print("Trop grand")