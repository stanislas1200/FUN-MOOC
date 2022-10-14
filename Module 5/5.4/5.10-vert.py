def dupliques(arr):
    for c in arr:
        if arr.count(c) > 1:
            return True
    return False
