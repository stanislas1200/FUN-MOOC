def decompresse(lst):
    """Decompresses a list of tuples into a list of words"""
    return [word for count, word in lst for i in range(count)]