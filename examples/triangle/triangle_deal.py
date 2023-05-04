import deal

@deal.pre(lambda _: _.x > 0 and _.y > 0 and _.z > 0)
@deal.post(lambda result: result in ["Equilateral triangle", "Isosceles triangle", "Scalene triangle"])
@deal.has()
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"