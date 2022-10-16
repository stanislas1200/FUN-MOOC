def my_insert(list, n):
    ret = list[:]
    if type(n) != int:
        return None
    if n > ret[-1]:
        ret.append(n)
    elif n < ret[0]:
        ret.insert(0, n)
    for i in range(len(ret)):
        if ret[i] < n < ret[i + 1] if (i + 1 < len(ret)) else False:
            ret.insert(i+1, n)
            return ret
    return ret