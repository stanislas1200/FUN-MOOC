x = float(input())
a, n, c = 1, 0, 0

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)

while abs(a) > 1e-6:
    a = (-1) ** n * x ** (2 * n + 1) / fact(2 * n + 1)
    c += a
    n += 1
c -= a
print(c)