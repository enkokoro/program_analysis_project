import deal

# if count is not zero, `item` appears in `items` at least once.
@deal.ensure(lambda _: _.result == _["v1"] or _.result == _["v2"])
# if count is zero, `item` is not in `items`
@deal.has()
def sneaky_div(v1: int, v2: int) -> int:
    if v1 > 10000:
        s = v1 / 0  # unused statement
    if v1 > v2:
        s = v1
    else:
        s = v2
    return s
