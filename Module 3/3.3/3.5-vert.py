a = int(input())
b = int(input())

print(not(((a/b) - int((a/b))) * 10) == 0 and not(((b/a) - int((b/a))) * 10) == 0)