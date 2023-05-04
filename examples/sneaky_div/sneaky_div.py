def sneaky_div(v1, v2):
    if v1 > 10000:
        s = v1 / 0  # unused statement
    if v1 > v2:
        s = v1
    else:
        s = v2
    return s
