nb = int(input())
for i in range(nb):
    for j in range(1,nb+1):
        print(j*(i+1), end="\t")
    print("")