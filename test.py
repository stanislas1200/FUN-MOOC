voyelles = "aeiouy"
x = list(enumerate('bonjour'))
i = 0
while i < len(x):
    if x[i][1] in voyelles:
        del x[i]
    else:
        i = i + 1

print(x)