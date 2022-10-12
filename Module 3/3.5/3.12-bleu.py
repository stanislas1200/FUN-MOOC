inputs = int(input())
for i in range(inputs):
    for j in range(inputs):
        if j < i:
            print(" ", end="")
        else :
            print("X", end="")
    print("")