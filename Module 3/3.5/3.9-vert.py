answerd = 0
while answerd != 42:
    answerd = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
    if answerd == 42:
        print("Bravo !")
    else:
        print("Mauvaise réponse.")