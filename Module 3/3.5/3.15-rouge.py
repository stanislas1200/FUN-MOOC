saut = int(input())
position_cible = int(input())
position_courante = 0
while position_courante + saut != 0:
    position_courante += saut
    if position_courante >= 100:
        position_courante %= 100
    if position_courante == position_cible:
        print("Cible atteinte")
        break
    print(position_courante)
    if position_courante == 0:
        print("Pas trouvée")
        break