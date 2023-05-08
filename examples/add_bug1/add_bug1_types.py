import deal

@deal.ensure(lambda _: _.result == _.a + _.b)
def add(a: int, b: int) -> int:
    return a - b 