def my_pow(m, b):
    return None if not(isinstance(m, int)) or not(isinstance(b, float)) else [b ** x for x in range(m)]

print(my_pow('a', 'b'))