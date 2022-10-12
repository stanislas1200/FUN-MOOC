x = int(input())

for i in range(1,x+1):
    for j in range(x-i):
        print(' ', end='')
    for j in range(i):
        print((i+j)%10,end="")
    for j in range(i-1, 0, -1):
        print((i+j-1)%10,end="")
    print("")