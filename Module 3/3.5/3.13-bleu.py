inputs = int(input())
res = 0
if int(inputs) >= 0:
    for i in range(inputs):
        res += int(input())
else :
    inputs = "0"
    while inputs != 'F':
        res += int(inputs)
        inputs = input()
print(res)