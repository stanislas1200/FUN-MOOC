def my_filter(lst, f):
    """Filters a list using a function"""
    return [item for item in lst if f(item)]