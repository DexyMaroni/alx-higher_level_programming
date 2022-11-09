def def add_integer(a, b=98):

    """This function adds two integers together and prints the sum."""

    if a not in [float, int]:
        raise TypeError ("a must be an integer")

    if b not in [float, int]:
        raise TypeError ("b must be an integer")

    if type(a) == float:
        a = int(a)

    if type(b) == float:
        b = int(b)
    

    return a+b
