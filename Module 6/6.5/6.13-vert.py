def next_line(line):
    """Returns the next line of Conway's ..."""
    if not line:
        return [1]
    count = 0
    val = line[0]
    res = []
    for n in line:
        if n == val:
            count += 1
        else:
            res.append(count)
            res.append(val)
            val = n
            count = 1
    res.append(count)
    res.append(val)
    return res