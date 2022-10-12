def rac_eq_2nd_deg(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return ()
    elif delta == 0:
        return -b/(2*a),
    else:
        r1 = (-b + delta**0.5)/(2*a)
        r2 = (-b - delta**0.5)/(2*a)
        return min(r1, r2), max(r1, r2)