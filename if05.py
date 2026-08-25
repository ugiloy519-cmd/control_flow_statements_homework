def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    if a < 0:
        return 1
    elif b < 0:
        return 1
    elif c < 0:
        return 1
    else:
        return 0

print(main(4,2,-7))

