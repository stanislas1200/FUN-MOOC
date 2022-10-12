polyèdre = input()
l = float(input())

if polyèdre[0] == 'T':
    print(((2**0.5)/12)*(l**3))
elif polyèdre[0] == 'C':
    print(l**3)
elif polyèdre[0] == 'O':
    print(((2**0.5)/3)*(l**3))
elif polyèdre[0] == 'D':
    print(((15+7*(5**0.5))/4)*(l**3))
elif polyèdre[0] == 'I':
    print(((5*(3+(5**0.5)))/12)*(l**3))
else:
    print("Polyèdre non connu")