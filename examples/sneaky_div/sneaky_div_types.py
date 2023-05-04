def sneaky_div(v1: int, v2: int) -> int:
    if v1 > 10000:
        s = v1 / 0  # unused statement
    if v1 > v2:
        s = v1
    else:
        s = v2
    return s
