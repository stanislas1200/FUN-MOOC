pari = int(input())
tirage = int(input())

if pari >= 0 and pari < 13 and pari == tirage :
    print(10*12)
elif pari == 13 and tirage % 2 == 0:
    print(10*2)
elif pari == 14 and tirage % 2 != 0:
    print(10*2)
elif pari == 15 and (tirage == 1 or tirage == 3 or tirage == 5 or tirage == 7 or tirage == 9 or tirage == 12):
    print(10*2)
elif pari == 16 and not(tirage == 1 or tirage == 3 or tirage == 5 or tirage == 7 or tirage == 9 or tirage == 12) and tirage != 0:
    print(10*2)
else :
    print(0)