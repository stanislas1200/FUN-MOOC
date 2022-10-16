def my_insert(list, n):
    assert isinstance(n, int)
    if n > list[-1]:
        list.append(n)
    elif n < list[0]:
        list.insert(0, n)
    for i in range(len(list)):
        if list[i] < n < list[i + 1] if (i + 1 < len(list)) else False:
            list.insert(i+1, n)