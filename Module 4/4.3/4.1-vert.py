def deux_egaux(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False


a = int(input())
b = int(input())
c = int(input())

print(deux_egaux(a, b, c))