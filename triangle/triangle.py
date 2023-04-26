"""
Categorizes triangle based on side lengths

Base Version
"""
def triangle(x, y, z):
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"